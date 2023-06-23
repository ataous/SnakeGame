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

    def create_snake(self):
        for i in range(3):
            self.squares.append(Turtle(shape="square"))
            self.squares[-1].penup()
            self.squares[-1].color("white")
            self.squares[-1].goto(i * (-SIZE), 0)
        self.head = self.squares[0]

    def add(self):
        self.squares.append(Turtle(shape="square"))
        self.squares[-1].penup()
        self.squares[-1].color("white")
        self.squares[-1].goto(self.squares[-1].position())

    def move(self):
        for i in range(len(self.squares) - 1, 0, -1):
            self.squares[i].goto(self.squares[i - 1].xcor(), self.squares[i - 1].ycor())

        self.head.forward(SIZE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def check_touch_tail(self):
        for square in self.squares[1:]:
            if square.distance(self.head) < 10:
                return True
        return False

    def reset(self):
        for square in self.squares:
            square.goto(1000, 1000)
        self.squares.clear()
        self.create_snake()

# Ens Of Snake Class
# -----------------------------------------------------------
