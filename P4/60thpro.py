#Arguments and keyword arguments

def super_func(*args):
    return sum(args)

print(super_func(1,2,3,4,5))

def super_func2(name, *args, i ='Awesome', **kwargs):
    total = 0
    for items in kwargs.values():
        total += items
    return sum(args) + total

print(super_func2('Abeneth', 1,2,3,4,5, num1 = 5, num2 = 10))

#Rule: Parameters come first, *arguments come second, default parametes come third and finally **kwargs or keyword arguments