from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

import time
my_snake = Snake()
food = Food()
sb = Scoreboard()

sc = Screen()
sc.setup(width=600, height=600)
sc.bgcolor("black")
sc.title("My Snake Game")
sc.tracer(0)
is_game_on = True
sc.listen()
sc.onkey(key="Up", fun=my_snake.up)
sc.onkey(key="Down", fun=my_snake.down)
sc.onkey(key="Right", fun=my_snake.right)
sc.onkey(key="Left", fun=my_snake.left)

while is_game_on:
    sc.update()
    time.sleep(0.1)
    my_snake.move()

#Detect collision with food

    if my_snake.head.distance(food) < 15:
        food.refresh()
        my_snake.extend_segment()
        sb.score_increase()

    #Detect collision with wall
    if my_snake.head.xcor() > 290 or my_snake.head.xcor() < -300 or my_snake.head.ycor() > 280 or my_snake.head.ycor() < -290:
        sb.reset()
        my_snake.reset()
        # is_game_on = False

    #Detect collision with tail
    # for segment in my_snake.segments:
    #     if segment == my_snake.head:
    #         pass
    #     elif my_snake.head.distance(segment) < 10:
    #         is_game_on = False
    #         sb.game_over()
    for segment in my_snake.segments[1:]:
        if my_snake.head.distance(segment) < 10:
            # is_game_on = False
            sb.reset()
            my_snake.reset()
            # sb.game_over()
sc.exitonclick()

