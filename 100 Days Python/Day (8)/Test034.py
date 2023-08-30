#Review
#Create function greet() with 3 print statements and call 

# def greet():
#     print("Hello Abeneth")
#     print("How are you?")
#     print("I hope you are good")

# greet()

def greet_with_name(name):
    print(f"Hello {name}")
    print("How are you?")
    print("I hope you are good")

name = input(str("Please enter your name? "))
greet_with_name(name)