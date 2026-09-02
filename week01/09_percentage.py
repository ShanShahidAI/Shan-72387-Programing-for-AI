
obtained_marks = float(input("Enter obtained marks: "))
total_marks = float(input("Enter total marks: "))

percentage = (obtained_marks / total_marks) * 100

percentage_rounded = round(percentage, 2)

print("Percentage is:", percentage_rounded)
