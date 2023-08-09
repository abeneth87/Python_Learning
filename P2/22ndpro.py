basket = ['x','a','b','c','d','e','a','c','e']
print('d' in basket)
print(basket.index('d')) # it is in index 4 of the list
print(basket.count('d')) # returns how many times d is there in the list
#basket.sort() #sort the items in the list
print(basket)
print(sorted(basket)) #sorted is a function that is called here
print(basket) #sorted function does not change the list
basket.reverse()
print(basket)
#Function is like assigning a temporary variable to hold the data and then change it once it is executed
print('\n')
new_basket = basket.copy() # we can also use the [:] to do the same thing using list indexing
new_basket.sort()
print(new_basket)
print(basket)
