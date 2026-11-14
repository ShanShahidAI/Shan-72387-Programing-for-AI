# Assignment 2: Patient Dataset Audit Toolkit

## Description
A Python and Pandas tool to audit, clean, and validate synthetic patient records without modifying raw data[cite: 7].
## Submitted Files
- `patient_dataset.py`: Core `PatientDataset` class.
- `demo.py`: Main demonstration script.
- `test_patient_dataset.py`: Unit tests with assertions.
- `README.md`: Documentation and decision summary.
- `AI_Use.md`: AI tools usage record.
- `data/personal_cases.csv`: Custom test cases for boundaries.

## Cleaning Rules
- **patient_id**: Stripped of spaces, non-empty, and unique.
- **department**: Uppercased, mapped to official names, missing set to `Unknown`.
- **age**: Kept within 0–120 inclusive; others set to missing.
- **heart_rate**: Kept within 30–220 inclusive; others set to missing.
- **Imputation**: Missing values filled using column medians from valid data only.

## Five Decisions
1. **Deep copy in `cleaned()`**: Keeps `self.raw` completely untouched.
2. **Deduplication before checking IDs**: Exact duplicates can be removed safely, but differing rows with the same ID mean bad data that needs human review.
3. **`errors='coerce'`**: Converts non-numeric text to `NaN` without crashing the program.
4. **Excluding invalid values before medians**: Stops extreme values (e.g., negative age) from biasing the median.
5. **Imputation flags**: Marks which values were filled so reviewers know they are not real clinical measurements.

## Run Commands
```bash
uv run python assignments/assignment-02/demo.py
uv run python assignments/assignment-02/test_patient_dataset.py
```

## Expected vs Actual (Supplied Data)
| Metric | Expected | Actual |
| :--- | :--- | :--- |
| Cleaned rows | 99 | 99 |
| Age median used | 52 | 52 |
| Heart-rate median used | 80.5 | 80.5 |
| Age imputed count | 11 | 11 |
| Heart-rate imputed count | 9 | 9 |

## Personal Test Cases: Prediction vs Actual
| Check | Predicted | Actual | Notes |
| :--- | :--- | :--- | :--- |
| Invalid age count | 0 | 0 | Text parsed as nonnumeric |
| Invalid heart rate | 1 | 1 | 250 is outside 30–220 |
| Age median used | 37.5 | 37.5 | Median of [0, 30, 45, 120] |
| Department mapping | GENERAL MEDICINE | GENERAL MEDICINE | 'Gen Med' mapped correctly |

## Known Limitations
1. Median imputation reduces data variation and is only a classroom simulation.
2. Hardcoded department mappings cannot recognize unlisted department names.