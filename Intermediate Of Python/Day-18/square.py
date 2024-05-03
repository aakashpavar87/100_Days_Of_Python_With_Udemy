from turtle import Turtle, Screen

tim = Turtle()
my_sc = Screen()
tim.shape("turtle")
tim.color("crimson")
for i in range(4):
    tim.forward(100)
    tim.right(90)
my_sc.exitonclick()
