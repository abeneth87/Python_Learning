import turtle
import random

screen = turtle.Screen()
t = turtle.Turtle()


# Function to generate a random RGB color
def random_color():
    r = random.random()
    g = random.random()
    b = random.random()
    return (r, g, b)


# Initial number of sides for the polygon
num_sides = 3
line_length = 100

for _ in range(3, 11):
    # Set a random pen color for each line
    t.pencolor(random_color())
    for _ in range(num_sides):
        t.forward(line_length)
        t.left(-360 / num_sides)

    # Increase the number of sides and adjust the angles
    num_sides += 1


# Close the turtle graphics window on click
screen.exitonclick()
