import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car_man = CarManager()

screen.listen()
screen.onkey(player.move, "Up")
sb = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_man.create_car()
    car_man.move_cars()
    if player.ycor() >= 280:
        player.reset_pos()
        sb.increase_level()
        car_man.increase_speed()

    for car in car_man.all_cars:
        if player.distance(car) < 20:
            sb.game_over()
            game_is_on = False
screen.exitonclick()
