import turtle
from turtle import Turtle, Screen
import random
tim = Turtle()
sc = Screen()
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        rgb = random_color()
        tim.color(rgb)
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


tim.speed(0)
draw_spirograph(5)
sc.exitonclick()
