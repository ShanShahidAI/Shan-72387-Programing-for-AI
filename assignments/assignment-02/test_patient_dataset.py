"""Test suite for PatientDataset."""

import json
from pathlib import Path
import pandas as pd
from patient_dataset import PatientDataset

BASE_DIR = Path(__file__).resolve().parent
SUPPLIED_CSV = BASE_DIR / "data" / "patients_messy.csv"


def run_tests():
    """Run required assertions."""
    ds = PatientDataset(SUPPLIED_CSV)

    # 1. Missing column test
    try:
        ds.validate_required(["patient_id", "wrong_col"])
        assert False, "Missing column not caught"
    except ValueError:
        pass

    # 2. Raw audit counts
    audit = ds.audit()
    assert audit["row_count"] == 100
    assert audit["exact_duplicate_count"] == 1

    # 3. Exact duplicate removal
    cleaned = ds.cleaned()
    assert len(cleaned) == 99

    # 4. Valid numeric bounds
    assert cleaned["age"].between(0, 120).all()
    assert cleaned["heart_rate"].between(30, 220).all()

    # 5. Imputation counts
    assert cleaned["age_imputed"].sum() == 11
    assert cleaned["heart_rate_imputed"].sum() == 9

    # 6. Reject conflicting IDs
    temp_csv = BASE_DIR / "data" / "temp.csv"
    pd.DataFrame(
        {
            "patient_id": ["P01", "P01"],
            "age": [30, 45],
            "heart_rate": [70, 80],
            "department": ["Cardio", "Neuro"],
        }
    ).to_csv(temp_csv, index=False)

    try:
        PatientDataset(temp_csv).cleaned()
        assert False, "Conflicting ID not caught"
    except ValueError:
        pass
    finally:
        if temp_csv.exists():
            temp_csv.unlink()

    # 7. Original data preserved
    raw_copy = ds.raw.copy()
    _ = ds.audit()
    _ = ds.cleaned()
    pd.testing.assert_frame_equal(ds.raw, raw_copy)

    # 8. Cleaned copy independence
    test_df = ds.cleaned()
    test_df.loc[0, "age"] = 999
    assert ds.raw.loc[0, "age"] != 999

    # 9. Verify JSON reload
    audit_file = BASE_DIR / "output" / "audit.json"
    ds.save_audit(audit_file)
    with open(audit_file, "r", encoding="utf-8") as f:
        assert json.load(f)["row_count"] == 100

    print("All tests passed.")


if __name__ == "__main__":
    run_tests()