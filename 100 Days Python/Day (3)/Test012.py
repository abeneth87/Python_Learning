# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = round(weight / height ** 2)

if bmi <= 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif 18.6 <= bmi <= 25.0:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif 25.1 <= bmi <= 30.0:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif 30.1 <= bmi <= 35.0:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")


# "Your BMI is 18, you are underweight."
# "Your BMI is 22, you have a normal weight."
# "Your BMI is 28, you are slightly overweight."
# "Your BMI is 33, you are obese."
# "Your BMI is 40, you are clinically obese."


    # Under 18.5 they are underweight
    # Over 18.5 but below 25 they have a normal weight
    # Over 25 but below 30 they are slightly overweight
    # Over 30 but below 35 they are obese
    # Above 35 they are clinically obese.
