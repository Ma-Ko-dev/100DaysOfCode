from turtle import Turtle
from random import choice, randint

# Constants to manipulate the behaviour faster
SPAWN_RANGE = (-250, 250)
SPEED_INCREASE = 10
SPEED_START = 5
# some pre generated random colors
COLORS = [
    (87, 124, 219), (67, 207, 207), (194, 192, 12), (165, 80, 135), (249, 160, 239), (128, 50, 103), (247, 169, 120),
    (186, 227, 152), (76, 9, 99), (49, 79, 83), (235, 181, 145), (26, 3, 169), (113, 106, 96), (98, 243, 243),
]


class Car:
    """Creates a new Car Object with the functionality to create new Turtle Objects that getting stored in a list."""

    def __init__(self):
        self.car_speed = SPEED_START
        self.car_list = []

    def create_car(self):
        """Creates by chance a new "car" Turtle and stores it in a list. The chance to create a car is 1 in 6.
           Takes no Arguments and returns nothing."""
        spawn_chance = randint(1, 6)
        if spawn_chance == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(1, 2)
            new_car.color(choice(COLORS))
            new_car.setpos(self.rand_position())
            self.car_list.append(new_car)

    def rand_position(self):
        """Function to generate and return a random position between a certain range. Takes no Arguments and returns
           a random position as integers."""
        return 325, randint(SPAWN_RANGE[0], SPAWN_RANGE[1])

    def move(self):
        """Moves all cars in the car_list by its car_speed. Takes no Arguments and returns nothing."""
        for car in self.car_list:
            new_x = car.xcor() - self.car_speed
            car.goto(new_x, car.ycor())

    def increase_speed(self):
        """Increases the car_speed variable by the constant SPEED_INCREASE. Takes no Arguments and returns nothing."""
        self.car_speed += SPEED_INCREASE
