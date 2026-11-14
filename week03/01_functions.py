def calculate_grade(marks):
    """Return A, B, C, D, or F based on specified mark boundaries.
    Args:
        marks: Numeric value representing student marks.
    Returns:
        String representing the letter grade.
    """
    if marks >= 85:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"
#Shan_72387_PFAI_Week03
print(calculate_grade(49))
def input_by_user():
    """Prompt the user to enter weight and height.
    Returns:
        A tuple containing weight in kg and height in meters.
    """
    weight = int(input("Enter Weight in Kg: "))
    height = int(input("Enter Height in Meters: "))
    return weight, height
#Shan_72387_PFAI_Week03
def calculate_bmi(weight, height):
    """Calculate and display the user's BMI and status category.
    Args:
        weight: Weight in kilograms.
        height: Height in meters.
    """
    BMI = (weight / height) ** 2
    print(BMI)
    if BMI < 30 and BMI > 25:
        print("User is Overweight")
    elif BMI < 25 and BMI > 18.5:
        print("User is Normal")
    elif BMI < 18.5:
        print("User is Underweight")
    else:
        print("obese")
#Shan_72387_PFAI_Week03
input_by_user()
calculate_bmi()
square = lambda number: number**2
#Shan_72387_PFAI_Week03
def calculate_avg(*marks):
    """Return the arithmetic mean of a non-empty marks list.
    Args:
    marks: Numeric marks to average.
    Returns:
    The arithmetic mean of the supplied marks.
    """
    return sum(marks) / len(marks)
#Shan_72387_PFAI_Week03
def format_student(**details):
    """Format and return a string describing what the student studies.
    Args:
        **details: Keyword arguments containing student details like name and program.
    Returns:
        A formatted string with the student's name and program.
    """
    return f"{details['name']}studies {details['program']}"
