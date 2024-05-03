from turtle import Turtle
FONT = ("Courier", 18, "normal")
ALIGN = "center"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("score.txt") as f:
            cont = f.read()
        self.high_score = int(cont)
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.clear()
        # self.high_score = self.file_score
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGN, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        with open("score.txt", mode="w") as file:
            file.write(str(self.high_score))
        self.score = 0
        self.update_score()

    def score_increase(self):
        self.score += 1
        self.update_score()
# def game_over(self):
#     self.goto(0, 0)
#     self.write("Game Over !", align=ALIGN, font=FONT)
    # self.clear()
