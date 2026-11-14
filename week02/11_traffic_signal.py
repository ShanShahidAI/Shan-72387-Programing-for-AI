
density = input("Enter traffic density (low, medium, high): ")
emergency = input("Is emergency vehicle present (yes/no): ")
#Shan_72387_PFAI_Week02
if density != "low" and density != "medium" and density != "high":
    print("Invalid try other.")
#Shan_72387_PFAI_Week02
elif emergency == "yes":
    print("Emergency override: route receives immediate green.")
#Shan_72387_PFAI_Week02
elif density == "low":
    print("Green light time: 20 seconds")
elif density == "medium":
    print("Green light time: 40 seconds")
elif density == "high":
    print("Green light time: 60 seconds")
