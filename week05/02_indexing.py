import numpy as np

data = np.array(
    [[10, 20, 30, 40], [50, 60, 70, 80], [90, 100, 110, 120], [130, 140, 150, 160]]
)

print("First row:")
print(data[0])
print()

print("Last column:")
print(data[:, -1])
print()

print("Middle 2 x 2 block:")
print(data[1:3, 1:3])
print()

print("Every second row:")
print(data[::2])
print()

print("Values greater than 75:")
print(data[data > 75])
print()

print("Values divisible by 20:")
print(data[data % 20 == 0])
