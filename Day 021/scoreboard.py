from turtle import Turtle

# Constants for modifying the Text
ALIGNMENT = "center"
FONT = ("Arial", 14, "bold")


class Scoreboard(Turtle):
    """Creating a Scoreboard Object. Its job is to print the Score on top of the Screen and a "Game Over" text when
       necessary. Needs no Arguments."""

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto((0, 275))
        self.update_text()

    def add_point(self):
        """Increments the displayed score by 1. Needs no Arguments."""
        self.score += 1
        self.clear()
        self.update_text()

    def update_text(self):
        """Writes the scoretext on top of the screen. Needs no Arguments."""
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        """Writes a red "GAME OVER" text in the middle of the screen. Needs no Arguments."""
        self.goto(0, 0)
        self.color("red")
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
