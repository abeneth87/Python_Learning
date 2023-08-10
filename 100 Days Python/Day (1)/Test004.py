#Switcharoo with a & b

a = input('a: ')
b = input('b: ')

c = b #Declare from left to right
b = a 
a = c

print('a: ' + a)
print('b: ' + b)