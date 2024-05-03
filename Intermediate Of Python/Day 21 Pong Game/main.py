from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

sc = Screen()
sc.setup(width=800, height=600)
sc.bgcolor("black")
sc.title("My Pong Game")
sc.tracer(0)

ball = Ball()
r_pdl = Paddle(350, 0)
l_pdl = Paddle(-350, 0)

sb = Scoreboard()

tim = Turtle()
tim.penup()
tim.goto(0, -300)
tim.hideturtle()
tim.pen(pensize=5, pencolor="white")
tim.setheading(90)

while tim.ycor() < 300:

    tim.pendown()
    tim.forward(20)
    tim.penup()
    tim.forward(20)

sc.listen()
sc.onkey(r_pdl.go_up, "Up")
sc.onkey(r_pdl.go_dn, "Down")
sc.onkey(l_pdl.go_up, "w")
sc.onkey(l_pdl.go_dn, "s")

is_game_on = True
while is_game_on:
    time.sleep(ball.move_speed)
    sc.update()
    ball.move()

    """Checking collision with wall"""
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    """Checking collision with paddle"""
    if (ball.distance(r_pdl) < 50 and ball.xcor() > 320) or (ball.distance(l_pdl) < 50 and ball.xcor() < -320):
        ball.bounce_x()
        ball.move_speed -= 0.01

    if ball.xcor() > 370:
        ball.reset_pos()
        sb.increase_l_score()
    if ball.xcor() < -370:
        ball.reset_pos()
        sb.increase_r_score()

sc.exitonclick()
