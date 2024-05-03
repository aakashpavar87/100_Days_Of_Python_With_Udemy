weight = float(input("Enter your weight : "))
height = float(input("Enter yuor height : "))
bmi_level = weight / height ** 2;
if bmi_level == 18.5:
    print("You are underweight.")
elif bmi_level >= 18.5 and bmi_level < 25 :
    print("You are normal weighted.")
elif bmi_level >= 25 and bmi_level < 30 :
    print("You are slightly overweight.")
elif bmi_level >= 30 and bmi_level < 35 :
    print("You are obese.")
elif bmi_level >= 35 :
    print("You are clinically obese")