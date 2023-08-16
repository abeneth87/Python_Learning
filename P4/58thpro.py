def is_even(num):
    if num % 2 == 0:
        return 'This is an Even number'
    else:
        return 'This is an Odd number'

def is_even_ver_2(num):
    if num % 2 == 0:
        return 'This is Even'
    else:
        return 'This is Odd'

input_number = int(input('Enter Any number: '))
print(is_even_ver_2(input_number))

# The None value you are seeing at the end of the code execution is because your is_even_ver_2 function does not have an explicit return statement in all branches. When you call this function, and the input number is even, the function prints "This is Even" but does not have a return statement. In Python, a function that doesn't have a return statement or an explicit return None statement will return None by default.