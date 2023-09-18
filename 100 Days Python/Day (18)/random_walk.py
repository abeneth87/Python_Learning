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

# Set the turtle's speed and initial position
line_length = 10
t.speed("fastest")
t.goto(0, 0)
t.pensize(10)

# Set a delay to slow down the drawing
turtle.delay(10)

# Define the number of steps and step size
num_steps = 300
step_size = 20

for _ in range(num_steps):
    # Set a random pen color for each step
    t.pencolor(random_color())
    # Generate a random angle in 90-degree increments (0, 90, 180, or 270)
    angle = random.randint(0, 3) * 90
    t.setheading(angle)
    t.forward(step_size)

# Close the turtle graphics window on click
screen.exitonclick()
