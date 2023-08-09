#Tuple is Immutable list

my_tuple = (1,2,3,4,5) # lat long for Uber location

print(my_tuple[1])
print(3 in my_tuple)

user = {
    'basket' :[1,2,3],
    (1,2) : ['a','b','c','d'],
    'greet' : 'hello', # keys on the left : Values on the right
    'age' : 20
}

print(user.items()) #returns a tuple
print(user[(1,2)])