import turtle

import pandas
import pandas as pd

# Load the CSV file with state data
data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()

# Create a screen
screen = turtle.Screen()
screen.title("U.S States Game")

# Load the map image as a shape
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Create a list to store correct guesses
correct_guesses = []

# Main game loop
while len(correct_guesses) < 50:
    # Get user input and convert to title case
    answer_state = screen.textinput(title=f"{len(correct_guesses)}/50 States Correct",
                                    prompt="What's another state name?").title()

    # Check if the guess is among the 50 states
    if answer_state == "Exit":
        missing_state = [state for state in all_states if state not in correct_guesses]
        # missing_state = []
        # for state in all_states:
        #     if state not in correct_guesses:
        #         missing_state.append(state)
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("missed_state_csv.csv")
        break  # Exit the game if the user types "Exit"

    if answer_state in data["state"].to_list():
        # Get the row corresponding to the guessed state
        state_data = data[data["state"] == answer_state]

        # Get the x and y coordinates of the state
        x_cor = int(state_data["x"])
        y_cor = int(state_data["y"])

        # Write the correct guess on the map
        correct_guesses.append(answer_state)
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        t.goto(x_cor, y_cor)
        t.write(answer_state)

# Close the turtle graphics window when done
screen.bye()
