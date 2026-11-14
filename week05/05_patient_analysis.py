import numpy as np
import os

patient_data = np.array(
    [
        [101, 45, 38.5, 100, 92],
        [102, 23, 36.8, 75, 98],
        [103, 67, 39.1, 110, 89],
        [104, 54, 37.0, 80, 96],
        [105, 34, 38.0, 95, 93],
        [106, 72, 36.5, 70, 97],
    ],
    dtype=float,
)

print("Shape:", patient_data.shape)
print("Dimensions:", patient_data.ndim)
print("Size:", patient_data.size)
print("Data type:", patient_data.dtype)

patient_ids = patient_data[:, 0].astype(int)
clinical = patient_data[:, 1:]

print("\nPatient IDs:")
print(patient_ids)

print("\nClinical Features:")
print(clinical)

print("\nAverage Age:", np.mean(clinical[:, 0]))
print("Feature Means:", np.mean(clinical, axis=0))


selected = patient_data[
    (patient_data[:, 1] > 60) & (patient_data[:, 2] > 38) & (patient_data[:, 4] < 94)
]

print("\nSelected Patients:")
print(selected)

high_risk_mask = (clinical[:, 1] > 38) & (clinical[:, 3] < 94)

high_risk_ids = patient_ids[high_risk_mask]

print("\nHigh Risk Count:", np.sum(high_risk_mask))
print("High Risk IDs:", high_risk_ids)

minimum = clinical.min(axis=0)
maximum = clinical.max(axis=0)

normalized = (clinical - minimum) / (maximum - minimum)

print("\nNormalized Features:")
print(normalized)

folder = os.path.dirname(__file__)

np.save(os.path.join(folder, "data", "patient_data.npy"), patient_data)

np.savetxt(
    os.path.join(folder, "output", "normalized_features.csv"), normalized, delimiter=","
)

assert normalized.shape == (6, 4)
assert np.all(normalized >= 0)
assert np.all(normalized <= 1)
assert np.issubdtype(high_risk_ids.dtype, np.integer)

print("\nAll tests passed!")
