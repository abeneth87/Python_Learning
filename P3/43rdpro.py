#iterable - list , dictionary, tuple, set, string
#iterate -> one by one check each item in the collection

user = {
    'name' : 'Abeneth',
    'age' : 35 ,
    'can_swim' : False
}
for item in user: #prints keys
    print(item)
print('')
for item in user.items(): #prints key value pair as tuple
    print(item)
print('')
for item in user.values(): #prints values
    print(item)
print('')
for item in user.keys(): #prints keys
    print(item)
print('')
for key, value in user.items(): #prints keys and values seperately
    print(key, value)