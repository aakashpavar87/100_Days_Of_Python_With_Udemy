from turtle import Turtle

FONT = ("Courier", 16, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.level = 1
        self.penup()
        self.goto(-240, 260)
        self.update_level()
        self.hideturtle()

    def update_level(self):
        self.clear()
        self.write(f"Level :{self.level}", align="center", font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_level()

    def game_over(self):
        game_over = Turtle()
        game_over.hideturtle()
        game_over.penup()
        game_over.write("Game Over !", align="center", font=FONT)

