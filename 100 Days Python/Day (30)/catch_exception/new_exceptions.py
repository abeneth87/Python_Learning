#self made exceptions

height = float(input("Height in mtrs: "))
weight = int(input("Weight in kg: "))

if height > 3:
    raise ValueError("Human Height should not be over 3 meters.")


bmi = weight / height ** 2

print(bmi)