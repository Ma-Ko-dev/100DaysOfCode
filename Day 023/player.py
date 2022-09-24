from turtle import Turtle

# constants for faster code manipulation and less magic numbers
# HEADING: 90 = North, 0 = East and so on
HEADING = 90
P_SPEED = 20
START_POS = (0, -280)


class Player(Turtle):
    """The Player class inherits from Turtle and gives some extra functions to move the Player."""

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(HEADING)
        self.penup()
        self.go_to_start()

    def move_forwards(self):
        """Moves the player by 20 points in the forward direction. Takes no Arguments and returns nothing."""
        self.forward(P_SPEED)

    def go_to_start(self):
        """Resets the player to the starting point. Takes no Arguments and returns nothing."""
        self.goto(START_POS)
