def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

input_number = int(input('Enter Any number: '))

if is_even(input_number):
    print('This is an Even number')
else:
    print('This is an Odd number')
