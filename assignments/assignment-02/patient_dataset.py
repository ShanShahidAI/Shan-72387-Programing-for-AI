"""Load, audit, and clean patient datasets."""

import json
from pathlib import Path

import numpy as np
import pandas as pd


class PatientDataset:
    """Manage a patient dataset."""

    REQUIRED_COLUMNS = ["patient_id", "age", "heart_rate", "department"]

    def __init__(self, path):
        """Load the CSV file."""
        self.path = Path(path)
        missing_markers = ["", "missing", "N/A", "-"]

        self.raw = pd.read_csv(
            self.path,
            na_values=missing_markers,
            dtype={"patient_id": "string"},
        )

    def validate_required(self, columns):
        """Check required columns."""
        missing = [col for col in columns if col not in self.raw.columns]

        if missing:
            raise ValueError(f"Missing required columns: {missing}")

    def audit(self):
        """Return a summary of the original data."""
        self.validate_required(self.REQUIRED_COLUMNS)

        missing_counts = {
            col: int(self.raw[col].isna().sum())
            for col in self.raw.columns
        }

        dedup_raw = self.raw.drop_duplicates()
        id_series = dedup_raw["patient_id"].dropna()

        invalid_value_counts = {}
        nonnumeric_counts = {}

        limits = {
            "age": (0, 120),
            "heart_rate": (30, 220),
        }

        for col, (low, high) in limits.items():
            values = pd.to_numeric(
                self.raw[col].dropna(), errors="coerce"
            )

            nonnumeric_counts[col] = int(values.isna().sum())
            values = values.dropna()

            invalid_value_counts[col] = int(
                ((values < low) | (values > high)).sum()
            )

        department_labels = sorted(
            str(value)
            for value in self.raw["department"].dropna().unique()
        )

        return {
            "row_count": int(len(self.raw)),
            "column_count": int(len(self.raw.columns)),
            "missing_counts": missing_counts,
            "exact_duplicate_count": int(self.raw.duplicated().sum()),
            "repeated_id_count": int(id_series.duplicated().sum()),
            "invalid_value_counts": invalid_value_counts,
            "nonnumeric_counts": nonnumeric_counts,
            "department_labels": department_labels,
        }

    def cleaned(self):
        """Return a cleaned copy of the data."""
        self.validate_required(self.REQUIRED_COLUMNS)

        df = self.raw.copy(deep=True)
        df = df.drop_duplicates().reset_index(drop=True)

        # Check patient IDs.
        df["patient_id"] = df["patient_id"].str.strip()

        if (
            df["patient_id"].isna().any()
            or (df["patient_id"] == "").any()
            or df["patient_id"].duplicated().any()
        ):
            raise ValueError(
                "Conflicting, empty, or missing patient_id detected."
            )

        # Standardize department names.
        df["department"] = (
            df["department"].astype("string").str.strip().str.upper()
        )

        dept_map = {
            "GEN MED": "GENERAL MEDICINE",
            "GENERAL MED": "GENERAL MEDICINE",
            "GENERAL-MED": "GENERAL MEDICINE",
            "CARDIO": "CARDIOLOGY",
        }

        df["department"] = df["department"].replace(dept_map)
        df["department"] = df["department"].fillna("Unknown")
        df.loc[df["department"] == "", "department"] = "Unknown"

        # Convert numbers and replace invalid values.
        limits = {
            "age": (0, 120),
            "heart_rate": (30, 220),
        }

        for col, (low, high) in limits.items():
            df[col] = pd.to_numeric(df[col], errors="coerce")
            df.loc[(df[col] < low) | (df[col] > high), col] = np.nan

        # Mark values that need filling.
        df["age_imputed"] = df["age"].isna()
        df["heart_rate_imputed"] = df["heart_rate"].isna()

        # Fill missing values with valid medians.
        for col in ["age", "heart_rate"]:
            valid_values = df[col].dropna()

            if valid_values.empty:
                raise ValueError(
                    f"No valid {col} entries to compute median."
                )

            df[col] = df[col].fillna(valid_values.median())

        return df

    def save_audit(self, path):
        """Save the audit as JSON."""
        out_path = Path(path)
        out_path.parent.mkdir(parents=True, exist_ok=True)

        with open(out_path, "w", encoding="utf-8") as file:
            json.dump(self.audit(), file, indent=4)
