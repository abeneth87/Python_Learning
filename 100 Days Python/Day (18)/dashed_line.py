import turtle
from turtle import Turtle

screen = turtle.Screen()
t = turtle.Turtle()

# Set the speed of the turtle
t.speed(1)

# Define the length of each dah and the gap between

dash_length = 5
gap_length = 1

# loop to draw dashed line

for i in range(50):
    t.forward(dash_length)
    t.penup()  # lifts the pen
    t.forward(gap_length)
    t.pendown()  # puts the pen down

# Close the turtle graphics
screen.exitonclick()