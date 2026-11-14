"""Exception handling exercises for invalid inputs and division."""


def get_valid_age():
    """Prompt user for age and handle invalid non-integer input."""
    try:
        age = int(input("Enter your age: "))
        print("Your age is:", age)
    except ValueError:
        print("Error: Please enter a valid integer for age.")

#Shan_72387_PFAI_Week03
def safe_divide():
    """Divide two user numbers while catching conversion and zero division errors."""
    try:
        numerator = float(input("\nNumerator: "))
        denominator = float(input("Denominator: "))
        result = numerator / denominator
    except ValueError:
        print("Error: Enter numeric values only.")
    except ZeroDivisionError:
        print("Error: The denominator cannot be zero.")
    else:
        print("Result:", result)

#Shan_72387_PFAI_Week03
# Run exercises
get_valid_age()
safe_divide()
