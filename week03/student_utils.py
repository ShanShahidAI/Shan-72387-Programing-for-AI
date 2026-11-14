"""Utility functions for calculating and formatting student marks."""

#Shan_72387_PFAI_Week03
def calculate_average(marks):
    """Return the arithmetic mean of a non-empty marks list.

    Args:
        marks: Numeric marks to average.

    Returns:
        The arithmetic mean of the supplied marks.
    """
    return sum(marks) / len(marks)

#Shan_72387_PFAI_Week03
def calculate_grade(marks):
    """Return letter grade based on numeric marks."""
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
def format_summary(student_name, average_score, final_grade):
    """Format a student summary into a readable string."""
    return f"Student: {student_name} | Average: {round(average_score, 2)} | Grade: {final_grade}"