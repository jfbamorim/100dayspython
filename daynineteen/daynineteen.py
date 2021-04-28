from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_fowards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def move_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)


def move_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.down()


screen.listen()
screen.onkey(move_fowards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(move_left, "a")
screen.onkey(move_right, "d")
screen.onkey(clear, "c")
screen.exitonclick()
