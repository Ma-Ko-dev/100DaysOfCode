from turtle import Turtle
from random import randint

FOOD_LEN = 0.5
FOOD_WID = 0.5


class Food(Turtle):
    """Creates a Food Object. Needs no Arguments."""

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(FOOD_LEN, FOOD_WID)
        self.speed("fastest")
        self.refresh()
        self.rand_color()

    def refresh(self):
        """Places itself on a random coordinate on the screen. Needs no Arguments."""
        random_x = randint(-275, 275)
        random_y = randint(-275, 275)
        self.rand_color()
        self.goto(random_x, random_y)

    def rand_color(self):
        """Creates a random color and sets the color to itself. Needs no arguments and returns nothing."""
        r = randint(1, 255)
        g = randint(1, 255)
        b = randint(1, 255)
        self.color((r, g, b))
