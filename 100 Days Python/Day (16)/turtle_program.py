# from turtle import Turtle, Screen
#
# abe = Turtle()
# print(abe)
# abe.shape("turtle")
# abe.color("green")
# abe.forward(100)
# abe.left(90)
# abe.forward(100)
# abe.left(90)
# abe.forward(100)
# abe.left(90)
# abe.forward(100)
# abe.left(90)
#
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()

table.field_names = ["Pokemon Name", "Type", ]
table.add_row(["Pikachu", "Electric", ])
table.add_row(["Squirtle", "Water", ])
table.add_row(["Charmander", "Fire", ])
table.align = "l"
print(table)