from turtle import Turtle, Screen
import random
# Several ways to import modules
# from turtle import *
# import turtle as t

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue",
           "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
movements = [0, 90, 180, 270]

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
# for _ in range(15):
#    timmy_the_turtle.forward(10)
#    timmy_the_turtle.penup()
#    timmy_the_turtle.forward(10)
#    timmy_the_turtle.pendown()

# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)

# Draw different shapes
# for i in range(3, 11):
#   j = i
#    #color = random.choices(range(255), k=3)
    #timmy_the_turtle.color(color)
#    while j > 0:
#        angle = 360 / i
#        timmy_the_turtle.forward(100)
#        timmy_the_turtle.right(angle)
#        j -= 1

# Generate a random walk
timmy_the_turtle.pensize(10)
for _ in range(200):
    timmy_the_turtle.speed("fastest")
    timmy_the_turtle.color(random.choice(colours))
    timmy_the_turtle.forward(30)
    timmy_the_turtle.setheading(random.choice(movements))


screen = Screen()
screen.exitonclick()
