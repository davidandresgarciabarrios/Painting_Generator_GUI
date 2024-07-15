# This script uses the colorgram.py library to extract colors from an image:
# import colorgram
#
# colors = colorgram.extract('Painting.jpg', 12)
#
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

import random
import turtle
from turtle import Turtle

colors_list = [
    (146, 199, 95),
    (252, 57, 151),
    (14, 135, 66),
    (225, 217, 180),
    (209, 226, 233),
    (164, 31, 94),
    (255, 215, 232),
    (236, 205, 141),
    (34, 126, 193),
    (0, 165, 131),
    (247, 230, 223),
    (233, 238, 234)
]

# Setting up the screen
turtle.colormode(255)

# Creating the turtle
spot = Turtle()
spot.penup()
spot.speed("fastest")

# Define the number of spots and their spacing
spots_x = 10
spots_y = 10
spacing = 50

# Position the turtle
start_x = -((spots_x - 1) * spacing) // 2
start_y = -((spots_y - 1) * spacing) // 2
spot.setpos(start_x, start_y)

# Create the grid of spots
for y in range(spots_y):
    for x in range(spots_x):
        spot.dot(20, random.choice(colors_list))
        spot.forward(spacing)
    spot.setpos(start_x, start_y + (y + 1) * spacing)

# Hide the turtle and display the window
spot.hideturtle()
turtle.exitonclick()
