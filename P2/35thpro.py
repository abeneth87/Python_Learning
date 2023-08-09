#set methods 2

my_set = {1,2,3,4,5,6}
your_set = {4,5,6,7,8,9,10}
large_set = my_set | your_set

print(my_set.issubset(your_set)) #Output ->False
print(my_set.issubset(large_set)) #Output ->True
print(large_set.issuperset(my_set)) #Output ->True

