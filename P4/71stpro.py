#lists comprehension

my_list = []

for char in 'hello':
    my_list.append(char)

print(my_list)

#This can be simplified using list comprehension through

my_new_list = [char for char in 'hakuhodo'] #param for param in 'Iterable'
my_new_list2 = [num for num in range(0,100)]
my_new_list3 = [num**2 for num in range(0,100)]
my_new_list4 = [num**2 for num in range(0,100) if num %2 == 0]
print(my_new_list4)