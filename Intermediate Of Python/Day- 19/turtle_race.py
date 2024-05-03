import random
from turtle import Turtle, Screen
sc = Screen()
sc.setup(width=500, height=400)
user_bet = sc.textinput(title="Make a Bet !", prompt="Which Turtle is going to win ? Choose a color : ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# tim = Turtle()
# tim.shape("turtle")
# tom = Turtle()
# jerry = Turtle()
# peter = Turtle()
# ben = Turtle()
# gwen = Turtle()
# turtles = [tim, tom, jerry, peter, ben, gwen]
turtles = []
step = 30
is_race_on = True

for i in range(6):
    tim = Turtle()
    turtles.append(tim)
    turtles[i].shape("turtle")
    turtles[i].color(colors[i])
    turtles[i].penup()
    turtles[i].goto(x=-230, y=(-125)+step)
    step += 30

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_turtle = turtle.pencolor()
            if user_bet == winning_turtle:
                print(f"You've won! The {winning_turtle} turtle is the Winner...")
            else:
                print(f"You've lost! The {winning_turtle} turtle is the Winner...")
        rand_dist = random.randint(0, 10)
        turtle.forward(rand_dist)

sc.exitonclick()
# sc.listen()
