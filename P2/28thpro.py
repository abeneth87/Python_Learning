#Dictionary continued
user = {
    'basket' :[1,2,3],
    'greet' : 'hello', # keys on the left : Values on the right
    'age' : 20
}
print('basket' in user)
print('size' in user)
print('age' in user.keys()) #keys search
print('hello' in user.values()) #values search
print(user.items()) # A Tuple in action

user2 = user.copy()
print(user.clear()) #Clears the contents of the list
print(user2) #But, still displays the contents as we have copied it 3 life ago

