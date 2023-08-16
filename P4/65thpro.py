#scope

def outer():
    x = "local"
    def inner():
        nonlocal x   # comment out this nonlocal syntax to see the difference
        x = "nonlocal"
        print("inner:", x)

    inner()
    print("Outer:", x) #Because of commenting out the above the outer goes to print "local"

outer()

#1 - Start with the local variable
#2 - refer the parent local
#3 - refer the global variable
#4 - built in python functions