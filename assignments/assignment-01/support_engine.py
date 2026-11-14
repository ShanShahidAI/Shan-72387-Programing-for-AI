"""Student Support System.

Checks student marks and attendance, then gives advice.
"""


def read_float(prompt, minimum, maximum):
    """Get a valid decimal number within a given range."""
    while True:
        user_input = input(prompt)
        try:
            value = float(user_input)
            if minimum <= value <= maximum:
                return value
            print(
                f"Invalid range. Please enter a value between {minimum} and {maximum}."
            )
        except ValueError:
            print("Invalid input. Please enter a numeric decimal value.")


def read_int(prompt, minimum):
    """Get a valid whole number greater than or equal to minimum."""
    while True:
        user_input = input(prompt)
        try:
            value = int(user_input)
            if value >= minimum:
                return value
            print(f"Invalid value. Please enter an integer of at least {minimum}.")
        except ValueError:
            print("Invalid input. Please enter a valid whole integer.")


def classify_support(attendance, assignment_average, missed_submissions):
    """Decide student priority level based on performance."""
    if attendance < 60 or missed_submissions >= 4:
        return "High priority"
    elif attendance < 75 or assignment_average < 60 or missed_submissions >= 2:
        return "Moderate priority"
    else:
        return "Routine monitoring"


def format_message(category):
    """Return the advice text for a priority level."""
    if category == "High priority":
        return "Immediate academic support is recommended."
    elif category == "Moderate priority":
        return "Monitor progress and provide targeted guidance."
    elif category == "Routine monitoring":
        return "Continue routine monitoring."
    return "Unknown category."


def main():
    """Run the student support program."""
    attendance = read_float("Attendance percentage: ", 0.0, 100.0)
    assignment_average = read_float("Assignment average: ", 0.0, 100.0)
    missed_submissions = read_int("Missed submissions: ", 0)

    category = classify_support(attendance, assignment_average, missed_submissions)
    advisory = format_message(category)

    print(f"Support category: {category}")
    print(f"Advisory: {advisory}")


if __name__ == "__main__":
    main()
