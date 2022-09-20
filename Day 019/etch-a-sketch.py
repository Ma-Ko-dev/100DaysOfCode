from turtle import Turtle, Screen

"""
W to move forward
S to move backward
A to turn left
D to turn right
C to clear the drawing

Click anywhere in the window to close the app.
"""


def move_forward():
    garry.forward(10)


def move_backwards():
    garry.forward(-10)


def rotate_ccw():
    garry.left(10)


def rotate_cw():
    garry.right(10)


def clear_screen():
    garry.clear()
    garry.penup()
    garry.home()
    garry.pendown()


garry = Turtle()
screen = Screen()

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=rotate_cw)
screen.onkey(key="a", fun=rotate_ccw)
screen.onkey(key="c", fun=clear_screen)


screen.exitonclick()
