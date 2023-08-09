#Break, Continue and Pass
my_list = [1,2,3]
for item in my_list:
    continue
    print(item) #This line is never reached as continue is before the print statement

i = 0
while i < len(my_list): #while loop require variable declaration and incrementation
    print(my_list[i])
    i += 1
    pass #just to put in as placehoder for development
    
    