from turtle import Screen, Turtle
import time
from Snake import Snake

# Create screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Create snake with three turtle instances
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.05)

    snake.move()
