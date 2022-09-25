from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from time import sleep

# CONSTANTS
HEIGHT = 600
WIDTH = 600

# Setup
screen = Screen()
screen.tracer(0)
screen.setup(WIDTH, HEIGHT)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.colormode(255)
game_on = True

# creating the snake, food and the scoreboard
snake = Snake()
food = Food()
score = Scoreboard()

# snake controls
screen.listen()
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

# move the snake forward
while game_on:
    screen.update()
    sleep(0.1)
    snake.move()

    # detect collision with food
    if snake.snake_head.distance(food) < 15:
        snake.extend()
        snake.set_color(food.color())
        # snake.moving_color(food.color(), 0)
        food.refresh()
        score.add_point()

    # detect collision with wall
    if snake.snake_head.xcor() > 280 or snake.snake_head.xcor() < -280 or snake.snake_head.ycor() > 280 or \
            snake.snake_head.ycor() < -280:
        # game_on = False
        # score.game_over()
        score.reset()
        snake.reset()

    # detect collision with tail, ignoring the head
    for part in snake.snake_parts[1:]:
        if snake.snake_head.distance(part) < 10:
            # game_on = False
            # score.game_over()
            score.reset()
            snake.reset()

screen.exitonclick()
