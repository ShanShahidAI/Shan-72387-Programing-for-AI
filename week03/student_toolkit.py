from student_utils import calculate_average, calculate_grade
#Shan_72387_PFAI_Week03
def parse_marks(text):
    """Convert comma-separated text into a validated list of marks.

    Raises:
        ValueError: If input is empty, a value is missing, non-numeric,
                    or outside the range 0 to 100.
    """
    if not text.strip():
        raise ValueError("Enter at least one mark.")

    parts = text.split(",")
    marks = []
#Shan_72387_PFAI_Week03
    for part in parts:
        cleaned_part = part.strip()
        if not cleaned_part:
            raise ValueError("A mark is missing between commas.")

        try:
            mark = float(cleaned_part)
        except ValueError:
            raise ValueError(f"'{cleaned_part}' is not a valid number.")

        if mark < 0 or mark > 100:
            raise ValueError("Every mark must be between 0 and 100.")

        marks.append(mark)

    return marks

#Shan_72387_PFAI_Week03
def generate_summary(name, marks):
    """Generate and return a multi-line report string for a student."""
    avg = calculate_average(marks)
    grade = calculate_grade(avg)

    report = (

        f"Name: {name}\n"
        f"Marks: {marks}\n"
        f"Average: {round(avg, 2)}\n"
        f"Grade: {grade}\n"
      
    )
    return report
#Shan_72387_PFAI_Week03
def save_report(filename, report):
    """Write the report to a UTF-8 text file."""
    with open(filename, "w", encoding="utf-8") as file:
        file.write(report)
