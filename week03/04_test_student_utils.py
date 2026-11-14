import student_utils
#Shan_72387_PFAI_Week03
assert student_utils.calculate_grade(85) == "A"
assert student_utils.calculate_grade(84) == "B"
assert student_utils.calculate_grade(70) == "B"
assert student_utils.calculate_grade(69) == "C"
assert student_utils.calculate_grade(50) == "D"
assert student_utils.calculate_grade(49) == "F"
#Shan_72387_PFAI_Week03
assert student_utils.calculate_average([60, 70, 80]) == 70.0
assert student_utils.calculate_average([0, 50, 85, 100]) == 58.75
#Shan_72387_PFAI_Week03
print("All assertion checks passed.")
