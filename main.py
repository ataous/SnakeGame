# -----------------------------------------------------------
# imports
# -----------------------------------------------------------
import time
from turtle import Screen

from food import Food
from scoreboard import Scoreboard
from snake import Snake

# -----------------------------------------------------------
# Global variables
# -----------------------------------------------------------
screen = Screen()
screen.setup(width=600, height=600)
screen.colormode(255)
screen.bgcolor(36, 41, 47)
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while True:
    snake.move()
    screen.update()
    time.sleep(0.2)

    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.add()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.rest()
        snake.reset()

    if snake.check_touch_tail():
        scoreboard.rest()
        snake.reset()
