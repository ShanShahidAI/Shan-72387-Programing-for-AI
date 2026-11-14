import numpy as np

marks = np.array([78, 85, 91, 66, 88])
matrix = np.arange(12).reshape(3, 4)
images = np.zeros((2, 4, 4))
identity = np.eye(4)
values = np.linspace(0, 1, 10)

arrays = [marks, matrix, images, identity, values]
#Shan_72387_PFAI_Week05
for arr in arrays:
    print("Shape:", arr.shape)
    print("number of dimension:", arr.ndim)
    print("size:", arr.size)
    print("dtype:", arr.dtype)
    print()

print("marks.shape is (5,) because it is a 1D array with 5 elements.")
print("matrix.shape is (3, 4) because it has 3 rows and 4 columns.")

print("matrix.size == 12:", matrix.size == 12)
print("images.number of dimension == 3:", images.ndim == 3)
