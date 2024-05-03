import turtle
import pandas

screen = turtle.Screen()
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []


while len(guessed_states) < 50:
    answer_state = screen.textinput(f"{len(guessed_states)}/50 Guessed Correct !", "Enter State Name : ").title()
    x_cor = data[data.state == answer_state].x
    y_cor = data[data.state == answer_state].y

    if answer_state == "Exit":
        missing_states = [name for name in all_states if name not in guessed_states]
        # for name in all_states:
        #     if name not in guessed_states:
        #         missing_states.append(name)

        df = pandas.DataFrame(missing_states)
        df.to_csv("missing_states.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(x_cor), int(y_cor))
        t.write(f"{answer_state}")
# screen.exitonclick()
