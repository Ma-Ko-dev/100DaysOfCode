from turtle import Screen
from player import Player
from car import Car
from scoreboard import Scoreboard
from time import sleep

# CONSTANTS
FINISH_LINE = 280

# setup
screen = Screen()
screen.setup(width=600, height=600)
screen.colormode(255)
screen.tracer(0)
game_go = True

# creating the player, a car object that manages all cars and the scoreboard
player = Player()
car = Car()
score = Scoreboard()

# controls
# added double controls for faster movement ;)
screen.listen()
screen.onkey(player.move_forwards, "Up")
screen.onkey(player.move_forwards, "w")

# game loop with manual update
while game_go:
    sleep(0.1)
    screen.update()

    # create more cars and move them
    car.create_car()
    car.move()

    # check if player reached the goal
    if player.ycor() > FINISH_LINE:
        # increasing the speed, resetting the player and increase the level on the scoreboard
        car.increase_speed()
        player.go_to_start()
        score.increase_level()

    # collision with car
    for vehicle in car.car_list:
        if vehicle.distance(player) < 20:
            # display game over and exiting the game loop
            score.game_over()
            game_go = False

screen.exitonclick()
