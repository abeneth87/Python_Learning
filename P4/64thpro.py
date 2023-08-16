#Scope

total = 0

def count():
    global total #declaring a global variable inside a function
    total += 1
    return total

count()
count()
count()
print(count())