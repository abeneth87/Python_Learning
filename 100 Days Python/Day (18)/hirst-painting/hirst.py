# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('images.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

import turtle
import random

# Define the list of colors
color_list = [(213, 154, 96), (52, 107, 132), (179, 77, 31), (202, 142, 31), (115, 155, 171), (124, 79, 99),
              (122, 175, 156), (229, 236, 239), (226, 198, 131), (242, 247, 244), (192, 87, 108), (11, 50, 64),
              (55, 38, 19), (45, 168, 126), (47, 127, 123), (200, 121, 143), (168, 21, 29), (228, 92, 77),
              (244, 162, 160), (38, 32, 35), (2, 25, 24), (78, 147, 171), (170, 23, 18), (19, 79, 90), (101, 126, 158),
              (235, 166, 171), (177, 204, 185), (49, 62, 84)]

# Create a screen
screen = turtle.Screen()

# Set up the turtle
t = turtle.Turtle()
#t.hideturtle()
#t.penup()
t.speed("fastest")

# Set the initial position
start_x, start_y = -250, 250  # Adjust as needed
t.goto(start_x, start_y)

# Define grid parameters
num_rows = 10
num_cols = 10
dot_size = 20
spacing = 50

# Draw the grid of dots
for row in range(num_rows):
    for col in range(num_cols):
        # Get a random color from the color_list
        color = random.choice(color_list)
        hex_color = "#{:02X}{:02X}{:02X}".format(*color)  # Convert RGB to hexadecimal

        # Draw the dot with the selected color
        t.color(hex_color)
        t.dot(dot_size)

        # Move to the next column
        t.forward(spacing)

    # Move to the next row
    t.backward(spacing * num_cols)  # Return to the beginning of the row
    t.right(90)  # Turn right to move to the next row
    t.forward(spacing)
    t.left(90)  # Turn left to prepare for the next row

# Close the turtle graphics window on click
screen.exitonclick()
