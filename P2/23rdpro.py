#tricks with list continued
basket = ['x','a','b','c','d','e','a','c','e']
print(len(basket)) #length of the list
basket.sort()
print(basket) #This method permanently sorts the list
print()
basket.reverse() #This reverses the last
print(basket)
print()
print(basket[::-1]) # Temporary Reverses the already reversed list
print(basket) #displays the original variable implemented with the method
