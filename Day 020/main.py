from turtle import Screen
from snake import Snake
import time

# CONSTANTS
HEIGHT = 600
WIDTH = 600

# Setup
screen = Screen()
screen.tracer(0)
screen.setup(WIDTH, HEIGHT)
screen.bgcolor("black")
screen.title("My Snake Game")
game_on = True

# creating the snake
snake = Snake()

# snake controls
screen.listen()
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

# move the snake forward
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

screen.exitonclick()
