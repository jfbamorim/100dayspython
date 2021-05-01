from turtle import Screen, Turtle
from Player import Player
from Scoreboard import Scoreboard
from Car_Manager import CarManager
import time

# Screen definitions
screen = Screen()
screen.bgcolor("white")
screen.setup(width=600, height=600)
screen.title("Turtle crossing capstone")
screen.tracer(0)

# Instance of player
player_turtle = Player()
score = Scoreboard()
cmanager = CarManager()

# Draw lines in screen
lines = Turtle()
lines.color("black")
lines.penup()
lines.goto(-300, -260)
y = 20
x = 20
while y < screen.window_height():
    times = 0
    while times < 15:
        lines.pendown()
        lines.forward(x)
        lines.penup()
        lines.forward(x)
        lines.pendown()
        times += 1
    new_y = lines.ycor() + 40
    lines.penup()
    lines.goto(-300, new_y)
    y += 40

# Listen to events
screen.listen()
screen.onkey(player_turtle.go_up, "Up")
screen.onkey(player_turtle.go_down, "Down")
screen.onkey(player_turtle.go_left, "Left")
screen.onkey(player_turtle.go_right, "Right")

# Game flow
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cmanager.generate_car()
    cmanager.move_cars()

    # Detect collision with the wall
    for car in cmanager.all_cars:
        if car.distance(player_turtle) < 20:
            game_is_on = False
            score.game_over()

    # Detect when player reaches top side
    if player_turtle.is_at_finish_line():
        score.increase_level()
        cmanager.level_up()
        player_turtle.go_to_start()


screen.exitonclick()
