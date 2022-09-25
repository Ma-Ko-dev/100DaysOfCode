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
        self.highscore = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto((0, 275))
        self.update_text()

    def add_point(self):
        """Increments the displayed score by 1. Needs no Arguments."""
        self.score += 1
        self.update_text()

    def update_text(self):
        """Writes the scoretext on top of the screen. Needs no Arguments."""
        self.fun_highscore("read")
        self.clear()
        self.write(f"Score: {self.score} High score: {self.highscore}", align=ALIGNMENT, font=FONT)

    def reset(self):
        """Resets the score text to 0 and updates the Highscore im necessary. Takes no Argument and returns nothing."""
        if self.score > self.highscore:
            self.highscore = self.score
            self.fun_highscore("write")
        self.score = 0
        self.update_text()

    def fun_highscore(self, operation: str):
        """Reads and Writes the new Highscore value in a file. Takes 1 string argument. "read" to read the Highscore,
           or "write" to write the new Highscore to a file. Returns nothing. Prints an error message incase the
           Argument is not recognized."""
        if operation == "read":
            with open("data.txt", mode="r") as file:
                self.highscore = int(file.read())
        elif operation == "write":
            with open("data.txt", mode="w") as file:
                file.write(str(self.highscore))
        else:
            print("DEBUG: Wrong operation Argument. Use 'read' or 'write'")


    # def game_over(self):
    #     """Writes a red "GAME OVER" text in the middle of the screen. Needs no Arguments."""
    #     self.goto(0, 0)
    #     self.color("red")
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)
