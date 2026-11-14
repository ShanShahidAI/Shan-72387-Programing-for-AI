#Shan_72387_PFAI_Week03
def average(a, b):
    return (a + b) / 2


def double(number):
    return number * 2
#Shan_72387_PFAI_Week03
try:
    age = int(input("Age: "))
    print("Entered age:", age)
except ValueError:
    print("Invalid input! Please enter a valid integer for age.")

#Shan_72387_PFAI_Week03
def calculate_grade(mark):
    if mark >= 85:
        return "A"
    elif mark >= 70:
        return "B"
    else:
        return "below B"
#Shan_72387_PFAI_Week03
students = [
    ("Ali", 88),
    ("Rafay", 73),
    ("Hamza", 62)
]
#Shan_72387_PFAI_Week03
for name, mark in students:
    grade = calculate_grade(mark)
    print(f"{name}: {grade}")