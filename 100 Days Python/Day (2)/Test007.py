# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
new_height = float(height)
new_weight = int(weight)

height_mul = new_height ** 2
bmi = new_weight / height_mul
print(int(bmi))