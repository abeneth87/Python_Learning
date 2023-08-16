#return inside the function
def sum(num1, num2):
    def another_func(n1,n2):
        return n1 + n2
    return another_func(num1,num2)

#Function should do one thing really well
#Should return something

total = sum(10,20)
print(sum(10,total))