#Driving license check

age = int(input('Enter your age: '))
# print(type(age))

#Method 1:
# legal_age = 'You are allowed to drive' if age >= 18 else 'You should apply for driving license'
# print(legal_age)

#Method 2:
if age >= 18:
    print('You are allowed to drive')
elif age <= 17:
    print('You should apply for driving license')

