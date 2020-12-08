from turtle import Turtle, Screen
# Several ways to import modules
# from turtle import *
# import turtle as t


def move_to_right():
    timmy_the_turtle.right(90)
    timmy_the_turtle.forward(100)


timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")
# advance turtle forward
# timmy_the_turtle.forward(100)
# turning turtle to south
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# for i in range(0, 3):
#    move_to_right()
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)

# Draw a dashed line - https://opentechschool.github.io/python-beginners/en/loops.html
for _ in range(15):
    timmy_the_turtle.forward(10)
    timmy_the_turtle.penup()
    timmy_the_turtle.forward(10)
    timmy_the_turtle.pendown()

# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)

screen = Screen()
screen.exitonclick()
