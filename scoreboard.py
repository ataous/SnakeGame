from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 18, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(x=0, y=260)
        self.update()
        return

    def update(self):
        self.write(arg=f"Score: {self.score}", align=ALIGN, font=FONT)
        return

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update()
        return

    def game_over(self):
        self.goto(x=0, y=0)
        self.write(arg="GAME OVER", align=ALIGN, font=FONT)
        return