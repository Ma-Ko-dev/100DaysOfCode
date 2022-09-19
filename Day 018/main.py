import turtle
import colorgram
from turtle import Turtle, Screen
from random import choice

# config
turtle.colormode(255)

# the turtle
garry = Turtle()
garry.shape("circle")
garry.color("black")

# The Task is:
# Extract common colors from a hirst painting and save it.
# Draw a painting, consisting of 10 * 10 colored dots in the extracted colors.
# Each dot has a size og 20 and is spaced apart by 50.

# extracted_color = []
#
# # getting 15 most common colors in the image
# colors = colorgram.extract("image.jpg", 15)
#
# for color in colors:
#     # I explicitly put rbg.r (etc.) into a tuple instead of just using the return of color.rgb because that was asked
#     # in the project.
#     extracted_color.append((color.rgb.r, color.rgb.g, color.rgb.b))
#
# print(extracted_color)

# these are the extracted colors (minus lots of white and shades of white) from our image
colors = [(132, 166, 204), (220, 148, 108), (197, 135, 148), (32, 41, 61), (163, 59, 49), (41, 106, 155),
          (141, 183, 162), (237, 211, 92), (148, 61, 68), (214, 83, 72), (35, 61, 56)]
# penup because we dont want to draw lines
garry.penup()
# drawingspeed of 10 is fast but not too fast
garry.speed(10)
# since our steps are in 50 and we want to draw 10 rows, 500 is our max_draw
max_draw = 500
# draw_p is the position of the turtle. we increment its y position by draw_steps later since we want them x
# steps apart
draw_p = 0
draw_steps = 50
# 20 is our size of the dot we are painting
dot_size = 20

# loop as long as max_draw is bigger than draw_p. Because draw_p is incremented in 50 steps, we can do it 10 times here
while max_draw > draw_p:
    # simple do this for loop 10 times
    for i in range(10):
        # turtle paints a dot in a already defined size and color
        garry.dot(dot_size, choice(colors))
        # move the turtle x steps
        garry.forward(draw_steps)
    # increment the draw_p by x and set the new position of our turtle accordingly
    draw_p += draw_steps
    garry.setpos(0, draw_p)
# at the end we hide the turtle
garry.hideturtle()

# keep it on the bottom
screen = Screen()
screen.exitonclick()
