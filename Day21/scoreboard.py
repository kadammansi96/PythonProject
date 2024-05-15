from turtle import Turtle
ALIGN = "center"
FONT = ('Courier', 20, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(x=0, y=270)
        self.color("white")
        self.write(f"Score = {self.score}", align=ALIGN, font=FONT)
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f"Score = {self.score}", align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGN, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score = {self.score}", align=ALIGN, font=FONT)
