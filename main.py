# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = weight / height ** 2
bmi_rounded = round(bmi)

result = f"Your BMI is {bmi_rounded}, you "
if bmi < 18.5:
    result += "are underweight."
elif bmi_rounded < 25:
    result += "have a normal weight."
elif bmi_rounded < 30:
    result += "are slightly overweight."
elif bmi_rounded < 35:
    result += "are obese."
else:
    result += "are clinically obese."

print(result)
# print(bmi, bmi_rounded)
