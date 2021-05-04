import turtle
import pandas

IMG = "blank_states_img.gif"
EXIT_CODE = "Exit"

screen = turtle.Screen()
screen.title("U.S.A States Game")
screen.addshape(IMG)
turtle.shape(IMG)

states_data = pandas.read_csv("50_states.csv")
all_states = states_data.state.to_list()
guessed_states = []

while len(guessed_states) < len(all_states):
    answer_state = screen.textinput(f"{len(guessed_states)}/{len(all_states)} states correct", "What's another state's name?").title()
    if answer_state in all_states:
        guessed_states.append(answer_state)
        new_turtle = turtle.Turtle()
        new_turtle.hideturtle()
        new_turtle.penup()
        single_state = states_data[states_data.state == answer_state]
        new_turtle.goto(float(single_state.x), float(single_state.y))
        print(single_state.state)
        new_turtle.write(single_state.state.item())
    if answer_state == EXIT_CODE:
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break


# Function to retrieve the x and y position in out screen after mouse click
# def get_mouse_click_coord(x, y):
#    print(x, y)


# turtle.onscreenclick(get_mouse_click_coord)
# turtle.mainloop()

screen.exitonclick()
