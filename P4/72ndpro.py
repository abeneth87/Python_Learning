#sets and dictionary comprehension

#This can be simplified using list comprehension through #Same as before

my_new_list = {char for char in 'hakuhodo'} #param for param in 'Iterable'
my_new_list2 = {num for num in range(0,100)}
my_new_list3 = [num**2 for num in range(0,100)]
my_new_list4 = {num**2 for num in range(0,100) if num %2 == 0}
print(my_new_list4)

simple_dict = {
    'a': 1,'b' : 2,'c' : 3,'d' :4 ,'e' : 5
}
my_dict = {key:value**2 for key,value in simple_dict.items()
           if value %2 ==0}

my_dict2 = {num:num*2 for num in [1,2,3]}

print(my_dict)
print(my_dict2)