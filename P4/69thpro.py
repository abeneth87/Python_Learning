#zip
my_list = [1,2,3,4,5] #list
you_list = (10,20,30,40,50) #Tuple
their_list = (7,6,5,4,3)
def only_odd(item):
    return item % 2 != 0


print(list(map(only_odd,my_list)))
print(list(filter(only_odd,my_list)))
print(list(zip(my_list,you_list,their_list)))
print(my_list)