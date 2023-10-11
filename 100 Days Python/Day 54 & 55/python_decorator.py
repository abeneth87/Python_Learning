import time


def delay_decorator(function):
    def wrapper_function():
        time.sleep(3)   #Do it first
        function()   #Do it after the one above

    return wrapper_function


@delay_decorator
def say_hello():
    print("Hello")

@delay_decorator
def say_bye():
    print("Bye")

@delay_decorator
def say_greeting():
    print("How are you?")


say_hello()
say_greeting()
say_bye()
