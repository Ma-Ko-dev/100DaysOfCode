from turtle import Turtle
from random import randint

FOOD_LEN = 0.5
FOOD_WID = 0.5
FOOD_COL = "blue"


class Food(Turtle):
    """Creates a Food Object. Needs no Arguments."""

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(FOOD_LEN, FOOD_WID)
        self.color(FOOD_COL)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """Places itself on a random coordinate on the screen. Needs no Arguments."""
        random_x = randint(-275, 275)
        random_y = randint(-275, 275)
        self.goto(random_x, random_y)