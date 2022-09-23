from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from time import sleep
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("The one and only Pong")
screen.tracer(0)

pencil = Turtle()
pencil.hideturtle()
pencil.penup()
pencil.setheading(90)
pencil.goto(0, -275)
pencil.pensize(2)
pencil.color("white")

for i in range(-275, 300, 25):
    pencil.pendown()
    pencil.forward(12.5)
    pencil.penup()
    pencil.forward(12.5)

game_on = True

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

while game_on:
    sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision with top/buttom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # bounce your ball!
        ball.bounce_y()

    # detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detect r paddle miss
    if ball.xcor() > 380:
        scoreboard.l_point()
        ball.reset_position()

    # detect l paddle miss
    if ball.xcor() < -380:
        scoreboard.r_point()
        ball.reset_position()


screen.exitonclick()
