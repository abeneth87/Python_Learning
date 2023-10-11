from flask import Flask

app = Flask(__name__)
print(__name__)

def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper

def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper

def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper

@app.route("/")
def hello_world():
    return "<h1 style ='text-align: center'><p>Hello, World!</p></h1>" \
            "<p> This is a test paragraph with an image of Abe.</p>" \
            "<img src = 'https://www.99corporates.com/DirectorImages/07207980.JPG'>" \
             "<img src = 'https://i.pinimg.com/originals/11/df/a8/11dfa88cf0194f13497cb7fb13af3b12.gif'>"


@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def say_bye():
    return "<p>Bye, World!</p>"
@app.route("/user/<name>/<int:age>")
def greet(name, age):
    return f"<h1 style ='text-align: center'> Hello {name} and you are {age} years old!</h1>"

if __name__ == "__main__":
    app.run(debug=True)
