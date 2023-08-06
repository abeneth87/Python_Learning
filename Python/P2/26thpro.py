#Dictionary
dictionary = {
    'g' : [1,2,3], # key - value
    'd' : 'hello', #unordered key value pair
    'm' : True
}
my_list = [
{
    'g' : [1,2,3], # key - value
    'd' : 'hello', #unordered key value pair
    'm' : True
},
{
    'g' : [4,5,6], # key - value
    'd' : 'bye', #unordered key value pair
    'm' : False
}]
print(my_list[0]['g'][2])
print(my_list[1]['g'][2])
print(dictionary['d'])
print(dictionary['g'][2])