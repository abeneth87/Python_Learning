from turtle import Turtle, Screen

abe = Turtle()
screen = Screen()


def move_forwards():
    abe.forward(10)

def move_backwards():
    abe.backward(10)

def turn_left():
    abe.left(10)

def turn_right():
    abe.right(10)

def clear():
    abe.clear()
    abe.penup()
    abe.home()
    abe.pendown()

screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear, "c")


screen.exitonclick()