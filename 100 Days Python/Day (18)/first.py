from turtle import Turtle, Screen


abe_the_turtle = Turtle()
abe_the_turtle.shape("turtle")
abe_the_turtle.color("brown")

for i in range(4):
    abe_the_turtle.forward(100)
    abe_the_turtle.left(90)

screen = Screen()
screen.exitonclick()
