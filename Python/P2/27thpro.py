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
    'greet' : 'hello'
}
print(user['basket'])
#print(user['age']) error line just for understanding
print(user.get('age'))