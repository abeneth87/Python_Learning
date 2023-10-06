# File not found

try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["key"])

except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Something")

except KeyError as error_message:
    print(f"The key{error_message} does not exist")

else:
    content = file.read()
    print(content)

finally:
    # raise TypeError("This is a made up error by Abe") #raise is a syntax to escalate all other keywords
    file.close()
    print("The file was closed")