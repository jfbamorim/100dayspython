####################################################################
# Day 16 - Intermediate - Object Oriented Programming (OOP)
####################################################################
# from turtle import Turtle, Screen

# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("blue")
# timmy.forward(100)

# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()

# no data on empty table
# print(table)
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charizard"])
table.add_column("Type", ["Eletric", "Water", "Fire"])
table.align = "l"
print(table)
