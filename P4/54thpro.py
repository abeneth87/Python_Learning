#Defining Functions
#positional parameters - declare
def say_hello(name = 'Mr.Cool', emoji = '😎'):
    print(f'Hello {name} {emoji}')


#positional arguments- call
say_hello('Abeneth', '😊')
say_hello('Ram', '😊')
say_hello('S', '😊')

#keyword arguments
say_hello(emoji= "😊", name = 'Cool')
say_hello('Abeneth')