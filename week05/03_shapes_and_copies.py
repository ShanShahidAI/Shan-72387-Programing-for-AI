import numpy as np

original = np.array([10, 20, 30, 40, 50])

view = original[1:4]
view[0] = 999

print("C1 Original:", original)

independent = original[1:4].copy()
independent[0] = 555

print("C2 Original:", original)
print("Independent:", independent)

values = np.arange(1, 13)

reshaped = values.reshape(3, 4)
print("\nReshaped:")
print(reshaped)
print("Shape:", reshaped.shape)

transposed = reshaped.T
print("\nTransposed:")
print(transposed)
print("Shape:", transposed.shape)

flattened = reshaped.flatten()
print("\nFlattened:")
print(flattened)
print("Shape:", flattened.shape)

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

vertical = np.vstack((a, b))
print("\nVertical:")
print(vertical)
print("Shape:", vertical.shape)

horizontal = np.hstack((a, b))
print("\nHorizontal:")
print(horizontal)
print("Shape:", horizontal.shape)

parts = np.split(np.arange(12), 3)

print("\nSplit:")
for part in parts:
    print(part, "Shape:", part.shape)

print("\nElement count:", values.size)
