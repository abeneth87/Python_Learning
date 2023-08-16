print("Welcome to the roller coaster!")
height = int(input("What is your height in cm?"))

if height >= 140:
    print('You are good to go on the roller coaster')
    age = int(input("What is your age? "))
    if age < 12:
        print("Please pay $5")
    elif age <=18:
        print("Please pay $7")
    else:
        print("Please pay $12")
else:
    print('You are not allowed')