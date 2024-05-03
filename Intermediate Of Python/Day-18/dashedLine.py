from turtle import Turtle, Screen

tim = Turtle()
my_sc = Screen()

# tim.forward(10)
# tim.penup()
# tim.forward(10)
for _ in range(10):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()
my_sc.exitonclick()
