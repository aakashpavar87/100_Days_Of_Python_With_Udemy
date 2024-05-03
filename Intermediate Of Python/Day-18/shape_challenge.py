from turtle import Turtle, Screen
tim = Turtle()
sc = Screen()
tim.penup()
tim.setx(50)
tim.sety(50)
tim.pendown()
tim.pen(fillcolor="black", pensize=2)
for _ in range(3):
    tim.pen(pencolor="red")
    tim.forward(100)
    tim.right(120)
for _ in range(4):
    tim.pen(pencolor="crimson")
    tim.forward(100)
    tim.right(90)
for _ in range(5):
    tim.pen(pencolor="blue")
    tim.forward(100)
    tim.right(72)
for _ in range(6):
    tim.pen(pencolor="green yellow")
    tim.forward(100)
    tim.right(60)
for _ in range(7):
    tim.pen(pencolor="medium turquoise")
    tim.forward(100)
    tim.right(51.43)
for _ in range(8):
    tim.pen(pencolor="magenta")
    tim.forward(100)
    tim.right(45)
for _ in range(9):
    tim.pen(pencolor="gold")
    tim.forward(100)
    tim.right(40)
for _ in range(10):
    tim.pen(pencolor="lime")
    tim.forward(100)
    tim.right(36)
sc.exitonclick()
