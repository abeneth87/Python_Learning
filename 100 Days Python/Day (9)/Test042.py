programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again.",
    }

#print(programming_dictionary["Bug"])

programming_dictionary["If"] = "A condition that checks and does the sequence on the IF condition"
#print(programming_dictionary)

#Wipe a dictionary using an empty declaration like programming_dictionary = {}

#Edit item in dictionary
programming_dictionary["Bug"] = "A moth in your computer"
#print(programming_dictionary["Bug"])

#loop through dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])