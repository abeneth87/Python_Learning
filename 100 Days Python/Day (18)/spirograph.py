import turtle
import random
import math

screen = turtle.Screen()
t = turtle.Turtle()


# Function to generate a random RGB color
def random_color():
    r = random.random()
    g = random.random()
    b = random.random()
    return (r, g, b)


# Set the turtle's speed and initial position
t.speed("fastest")
t.pensize(2)

# Set a delay to slow down the drawing
turtle.delay(10)

# Define the number of circles and step size
num_circles = 60  # You can adjust this value for more or fewer circles
step_size = 10

for _ in range(num_circles):
    # Set a random pen color for each circle
    t.pencolor(random_color())

    # Generate a random radius for the circle
    radius = 100 #

    # Draw the circle
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.circle(radius)

    # Rotate the turtle to create the spirograph effect
    t.right(360 / num_circles)

# Close the turtle graphics window on click
screen.exitonclick()
