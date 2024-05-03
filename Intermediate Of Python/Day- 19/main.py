from turtle import Turtle, Screen
tim = Turtle()
sc = Screen()
sc.listen()


def forwards():
    tim.forward(10)


def backwards():
    tim.backward(10)


def clock_wise():
    new_head = tim.heading() + 10
    tim.setheading(new_head)


def counter_wise():
    new_head = tim.heading() - 10
    tim.setheading(new_head)


def clear_sc():
    tim.clear()
    tim.penup()
    tim.home()
    tim.down()


sc.onkey(key="w", fun=forwards)
sc.onkey(key="s", fun=backwards)
sc.onkey(key="a", fun=counter_wise)
sc.onkey(key="d", fun=clock_wise)
sc.onkey(key="c", fun=clear_sc)
sc.exitonclick()
