"""Run PatientDataset audit and cleaning demonstration."""

from pathlib import Path
import pandas.errors
from patient_dataset import PatientDataset


def main():
    """Execute audit, cleaning, and export pipeline."""
    base_dir = Path(__file__).resolve().parent
    input_file = base_dir / "data" / "patients_messy.csv"
    output_dir = base_dir / "output"

    try:
        dataset = PatientDataset(input_file)

        # 1. Audit original data
        audit_res = dataset.audit()
        print("Patient Dataset Audit")
        print(f"Original rows: {audit_res['row_count']}")
        print(f"Exact duplicates to remove: {audit_res['exact_duplicate_count']}")
        print(f"Invalid age values: {audit_res['invalid_value_counts']['age']}")
        print(f"Invalid heart-rate values: {audit_res['invalid_value_counts']['heart_rate']}")

        # 2. Clean data
        cleaned_df = dataset.cleaned()
        print("\nCleaning completed")
        print(f"Cleaned rows: {len(cleaned_df)}")
        print(f"Age values imputed: {cleaned_df['age_imputed'].sum()}")
        print(f"Heart-rate values imputed: {cleaned_df['heart_rate_imputed'].sum()}")

        # 3. Save outputs
        audit_file = output_dir / "audit.json"
        clean_file = output_dir / "patients_clean.csv"

        dataset.save_audit(audit_file)
        cleaned_df.to_csv(clean_file, index=False)

        print(f"\nSaved: {audit_file.relative_to(base_dir)}")
        print(f"Saved: {clean_file.relative_to(base_dir)}")

    except FileNotFoundError:
        print(f"Error: Missing file at {input_file}")
    except (pandas.errors.EmptyDataError, pandas.errors.ParserError) as err:
        print(f"CSV Parsing Error: {err}")
    except ValueError as err:
        print(f"Validation Error: {err}")
    except OSError as err:
        print(f"File System Error: {err}")


if __name__ == "__main__":
    main()