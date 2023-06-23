from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 18, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(x=0, y=260)
        self.update()
        return

    def update(self):
        self.clear()
        self.write(arg=f"Score: {self.score}  High Score: {self.high_score}", align=ALIGN, font=FONT)
        return

    def increase_score(self):
        self.score += 1
        self.update()
        return

    def rest(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update()

    def game_over(self):
        self.goto(x=0, y=0)
        self.write(arg="GAME OVER", align=ALIGN, font=FONT)
        return
