import numpy as np

# Error: (3,4) and (3,2) arrays cannot be added.
# Cause: Their shapes are different and cannot be broadcast together.
# Fix: Make b have the same shape as a.

a = np.ones((3, 4))
b = np.ones((3, 4))

result = a + b

print("F1 Result:")
print(result)

# Error: 'and' cannot be used with NumPy arrays.
# Cause: NumPy needs element-wise Boolean operators.
# Fix: Use & and put each condition in parentheses.

values = np.array([10, 20, 30, 40])

selected = values[(values > 15) & (values < 35)]

print("\nF2 Result:")
print(selected)

# Error: axis=0 calculates the average of each column.
# Cause: We need one average for each student/row.
# Fix: Use axis=1.

scores = np.array([[70, 80, 90], [60, 75, 85]])

student_averages = np.mean(scores, axis=1)

print("\nF3 Result:")
print(student_averages)
