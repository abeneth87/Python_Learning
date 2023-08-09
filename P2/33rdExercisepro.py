
#convert set in to a list of unique items

my_set = {1,1,2,3,4,3,4,5,6,8,2,5,3,4,1,5,7}


print(set(my_set))

new_set = my_set.copy() # creates copy
my_set.clear() # clears copy
print(len(my_set))
print(len(new_set))