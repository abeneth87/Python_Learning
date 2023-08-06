#Formatted string

name = 'Abeneth'
age = 35

print('Hi ' + name + ' Welcome to our website.' 'You are ' + str(age) +' years old.')
print(f'Hi {name}  Welcome to our website.' 'You are {age} years old.')
print('Hi {} Welcome to our website.' 'You are {} years old.'.format('Abe','35'))
print('Hi {} Welcome to our website.' 'You are {} years old.'.format(name,age))