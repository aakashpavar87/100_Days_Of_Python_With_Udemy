from turtle import Turtle, Screen
import random
t = Turtle()
sc = Screen()
colors = ["red", "blue", "green yellow", "magenta", "crimson", "blue", "medium turquoise", "gold", "lime"]


def draw_shape(shape_sides):
    angles = 360 / shape_sides
    for _ in range(shape_sides):
        t.forward(100)
        t.right(angles)


for shape_draw in range(3, 11):
    t.color(random.choice(colors))
    draw_shape(shape_draw)

