from turtle import Turtle
from random import randint
START_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DIST = 20


class Snake:
    """Creates a new Snake Object via Snake(). Takes no Arguments."""

    def __init__(self):
        self.snake_parts = []
        self.create_snake()
        self.snake_head = self.snake_parts[0]

    def create_snake(self):
        """Creates a Snake body with as many parts as defined in START_POS. Takes no arguments and returns nothing."""
        for pos in START_POS:
            self.add_part(pos)

    def add_part(self, pos):
        """Creates a new part of the turtle and adds it to the end of the snake_part list. Takes a position as
           Argument. """
        new_part = Turtle("square")
        new_part.penup()
        new_part.color(self.rand_color())
        new_part.setpos(pos)
        self.snake_parts.append(new_part)

    def extend(self):
        """Extends the snake by 1 new part by calling the add_part function."""
        self.add_part(self.snake_parts[-1].position())

    # moving the snake by moving the snake_head forwards and let every other snake_part "follow" the head
    def move(self):
        """Moves the Snake by a distance of MOVE_DIST. Takes no arguments and returns nothing."""
        for part in range(len(self.snake_parts) - 1, 0, -1):
            new_x = self.snake_parts[part - 1].xcor()
            new_y = self.snake_parts[part - 1].ycor()
            self.snake_parts[part].goto(new_x, new_y)
        self.snake_head.forward(MOVE_DIST)

    # the control part of the snake starts here. In my opinion, left and right is enough and saves us a lot of control
    # structure.
    def left(self):
        """Turns the Snake head by 90 degree to the left. Takes no Argument and returns nothing."""
        self.snake_head.left(90)

    def right(self):
        """Turns the Snake head by 90 degree to the right. Takes no Argument and returns nothing."""
        self.snake_head.right(90)

    def set_color(self, col):
        """Sets the color of the last snake part to the color of the last eaten food. Takes a color as Argument and
           returns nothing."""
        r = int(col[0][0])
        g = int(col[0][1])
        b = int(col[0][2])
        self.snake_parts[-1].color(r, g, b)

    def rand_color(self):
        """Creates a random color and returns it."""
        r = randint(1, 255)
        g = randint(1, 255)
        b = randint(1, 255)
        return r, g, b

