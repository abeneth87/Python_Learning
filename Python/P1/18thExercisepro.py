#Exercise to display the password length and display it as *

user_name = input('Enter your user name:')
password = input('Enter your password:')
pass_len = len(password)
pass_char = '*' * pass_len

print(f'Hi {user_name}, Your password {pass_char} is {pass_len} long character!, Am I right?')