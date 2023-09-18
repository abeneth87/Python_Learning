# Turtle racing game
import random
import turtle
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
user_guess = screen.textinput(title="Make your bet", prompt=f"Choose the color from {colors}")

y_position = [-70, -40, -10, 20, 50, 80]
all_turtles = []

# Create the turtles and set their initial positions
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    all_turtles.append(new_turtle)

# Check if the user made a bet
if user_guess:
    is_race_on = True
else:
    is_race_on = False

while is_race_on:
    for turtle in all_turtles:
        # Move each turtle forward by a random distance
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

        # Check if a turtle has crossed the finish line (x-coordinate >= 230)
        # ( Since turtle is 40 x 40, therefore 250 - (40/2) = 230 )
        if turtle.xcor() >= 230:
            winning_color = turtle.pencolor()
            if winning_color == user_guess:
                print(f"You've won! The {winning_color} turtle is the winner.")
            else:
                print(f"You've lost. The {winning_color} turtle is the winner.")
            is_race_on = False

# Close the turtle graphics window on click
screen.exitonclick()
