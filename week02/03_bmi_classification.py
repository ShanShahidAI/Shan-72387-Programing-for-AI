weight = float(input("Enter weight (kg): "))
height = float(input("Enter height (meters): "))
#Shan_72387_PFAI_Week02
bmi = weight / (height ** 2)

print("BMI =", bmi)
#Shan_72387_PFAI_Week02
if bmi < 18.5:
    print("Underweight---")
elif bmi < 25:
    print("Normal---")
elif bmi < 30:
    print("Overweight---")
else:
    print("Obese---")
    #Shan_72387_PFAI_Week02