import random
from turtle import Turtle, Screen
t = Turtle()
sc = Screen()
t.pen(pensize=3)
t.speed(8)
direction = ["right", "left", "back"]
colors = ["red", "blue", "green yellow", "magenta", "crimson", "blue", "medium turquoise", "gold", "lime"]
for _ in range(100):
    move = random.choice(direction)
    t.color(random.choice(colors))
    if move == "right":
        t.right(90)
    elif move == "left":
        t.left(90)
    else:
        t.back(10)
    t.forward(10)
    size_of_pen = 5
    t.pen(pensize=size_of_pen)
    size_of_pen += 1
sc.exitonclick()
