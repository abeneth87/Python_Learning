#Scope - 

a = 1                           #3 - refer global variable

def parent():
     a = 10                     # 2 - refer the parent local
     def confusion():ddd
        #return a                # 1 - a is inside the parent so it is self referencing 
        return sum              # 4 - Python built in function
     return confusion()

print(a)
print(parent())
print(a)

#1 - Start with the local variable
#2 - refer the parent local
#3 - refer the global variable
#4 - built in python functions