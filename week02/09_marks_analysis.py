
marks = [78, 65, 92, 85, 48, 91]

passing_marks = [m for m in marks if m >= 50]
failing_marks = [m for m in marks if m < 50]

average = sum(marks) / 6
highest = max(marks)
lowest = min(marks)

print("Passing:", passing_marks)
print("Failing:", failing_marks)
print("Average:", average)
print("Highest:", highest)
print("Lowest:", lowest)
