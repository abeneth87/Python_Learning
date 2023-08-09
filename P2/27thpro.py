#Dictionary Keys
dictionary ={
    123 : [1,2,3],
    True : 'Abeneth',
    #[100] : [1,4,5]  #Unhashable type
}

print(dictionary[True])


#dictionary 2

user = {
    'basket' : [1,2,3],
    'greet' : 'hello',
    'age' : 20
}

user2 = dict(name = 'AbeRam')
print(user['basket'])
#print(user['age']) error line just for understanding
print(user.get('age', 18)) # the 18 here is a added default value to stop returning null incase the data is not there in the dictionary
print(user2)