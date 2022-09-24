from turtle import Turtle

# Constants for faster manipulating some code
ALIGN = "center"
FONT = ("Arial", 14, "bold")


class Scoreboard(Turtle):
    """Displays the current Level and can display a GAME OVER text when necessary."""

    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.ht()
        self.penup()
        self.goto(-255, 275)
        self.update_text()

    def update_text(self):
        """Updates the current Level. Takes no Arguments and returns nothing."""
        self.write(f"Level: {self.level}", align=ALIGN, font=FONT)

    def increase_level(self):
        """Increases the current level by 1, clears itself and calls update_text() to display the new level.
           Takes no Arguments and returns nothing."""
        self.level += 1
        self.clear()
        self.update_text()

    def game_over(self):
        """Displays a red GAME OVER text in the middle of the screen. Takes no Arguments and returns nothing."""
        self.goto(0, 0)
        self.color("red")
        self.write("GAME OVER", align=ALIGN, font=FONT)
