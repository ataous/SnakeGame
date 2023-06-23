# -----------------------------------------------------------
# imports
# -----------------------------------------------------------
from turtle import Turtle

# -----------------------------------------------------------
# Constants
# -----------------------------------------------------------
SIZE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


# -----------------------------------------------------------
# Snake Class
# -----------------------------------------------------------
class Snake:

    def __init__(self):
        self.squares = []
        self.create_snake()
        self.head = self.squares[0]
        return

    def create_snake(self):
        for i in range(3):
            self.squares.append(Turtle(shape="square"))
            self.squares[i].penup()
            self.squares[i].color("white")
            self.squares[i].goto(i * (-SIZE), 0)
        return

    def add(self):
        i = len(self.squares)
        self.squares.append(Turtle(shape="square"))
        self.squares[i].penup()
        self.squares[i].color("white")
        self.squares[i].goto(self.squares[-1].position())

    def move(self):
        for i in range(len(self.squares) - 1, 0, -1):
            self.squares[i].goto(self.squares[i - 1].xcor(), self.squares[i - 1].ycor())

        self.head.forward(SIZE)
        return

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
        return

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
        return

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
        return

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
        return

    def check_touch_tail(self):
        for square in self.squares[1:]:
            if square.distance(self.head) < 10:
                return True
        return False

#  Ens Of Snake Class
# -----------------------------------------------------------
