#set methods

my_set = {1,2,3,4,5,6}
your_set = {4,5,6,7,8,9,10}

print(my_set.difference(your_set)) #Output -> {1, 2, 3}
print(my_set.discard(5)) #output -> None
print(my_set) #output -> {1, 2, 3, 4, 6}

# print(my_set.difference_update(your_set)) #Output -> None
# print(my_set) #Output -> {1, 2, 3}

print(my_set.intersection(your_set))
print(my_set & your_set)

print(my_set.isdisjoint(your_set)) # returns boolean value of the condition. Here it is false

print(my_set.union(your_set))
print(my_set | your_set)
