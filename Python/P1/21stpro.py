basket = [1,2,3,4,5]
# print(len(basket))

#Adding
basket.append(100)
print(basket)
#Inserting
basket.insert(3,3.5)
#new_list = basket
# print(basket)

#Extends
basket.extend([200,300])
# print(basket)

#removing
basket.pop() # pop removes the index
print(basket)
basket.pop(0) # pop removes the index
print(basket)
basket.remove(3.5)
print(basket)
basket.clear()
print(basket)