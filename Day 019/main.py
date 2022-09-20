from turtle import Turtle, Screen
from random import randint

# constants
WIDTH = 500
HEIGHT = 400
FINISH_LINE = 230
START_X = -(WIDTH / 2) + 15

# setup
screen = Screen()
screen.setup(WIDTH, HEIGHT)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
total_turtle = []
race_on = False
winner = ""
y_pos = 70
y_step = 30

# take the bet
bet = screen.textinput("Place your bet now!", f"Input a color from the list without quotation marks: \n{*colors,}")

# create the turtles
for c in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(c)
    new_turtle.goto(x=START_X, y=y_pos)
    y_pos -= y_step
    total_turtle.append(new_turtle)

# start the race when everything is set up and if we have a bet form the user
if bet and bet in colors:
    race_on = True

# the actual race happens here. everything starts when race_on is True
while race_on:
    for t in total_turtle:
        # loop through the list of all turtles
        if t.xcor() >= FINISH_LINE:
            # check if one of the turtles reached the finish line
            winner = t.pencolor()
            # stopping the race
            race_on = False
            # check if the user won
            if bet == winner:
                print(f"The {winner} turtle won. You have won your bet!")
            else:
                print(f"The {winner} turtle won. You lost your bet!")
        # moving the turtle forward a random amount
        t.forward(randint(0, 10))
