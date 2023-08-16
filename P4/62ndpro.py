#Scope - What variables do I have access to?
#Python has functional scope. Anything that is decalared inside function is not called unless it is declared

if True:
    x = 10

def some_func():
    total = 100
    return total

print(some_func())

#Notice the "a" variable
a = 1

def confusion():
    a = 5
    return a

print(a)
print(confusion())
print(a)
