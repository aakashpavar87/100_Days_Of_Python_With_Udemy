import random
import turtle
from turtle import Turtle, Screen

t = Turtle()
turtle.colormode(255)
sc = Screen()
t.pen(pensize=9)
t.speed(0)
direction = [0, 90, 180, 270]


# colors = ["red", "blue", "green yellow", "magenta", "crimson", "blue", "medium turquoise", "gold", "lime"]


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


for _ in range(200):
    t.setheading(random.choice(direction))
    t.color(random_color())
    t.forward(20)
sc.exitonclick()
