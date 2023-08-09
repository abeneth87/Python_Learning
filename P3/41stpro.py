print(True == 1)
print('' == 1) #Truthy vs Falsey
print([] == 1) #Truthy vs Falsey
print(10 == 10.0)
print( [] == [])

print(True is 1) #False 
print('' is 1) #False
print([] is 1) #False
print(10 is 10.0) #False
print( [] is []) #False

#All of the second checks whether the memory allocation is same for both

a = [1,2,3]
b = [1,2,3]
print('')
print(10 is 10) #True since it is stored in same place
print (a == b) #True
print (a is b) #False