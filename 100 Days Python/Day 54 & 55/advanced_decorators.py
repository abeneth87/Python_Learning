class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False

def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in:
            return function(*args, **kwargs)  # Call the function and return its result
        else:
            print("User is not logged in.")  # Add an authentication message
    return wrapper  # Return the wrapper function

@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s latest blog post.")

new_user = User("Abeneth")
new_user.is_logged_in = True
create_blog_post(new_user)
