import colorgram as cg
import turtle as tl
from turtle import Turtle, Screen
import random

# colors = cg.extract('Veil-of-Loves-Everlasting.jpg', 15)

# rgb_colors = [((item.rgb.r, item.rgb.g, item.rgb.b))
#               for item in colors]

# # first_color = colors[0]
# # rgb = first_color.rgb
# # hsl = first_color.hsl
# # proportion = first_color.proportion

# print(len(rgb_colors))

toby = Turtle()
tl.colormode(255)
toby.speed("fastest")

color_list = [(238, 236, 234), (213, 156, 90), (135, 170, 202), (196, 136, 155), (235, 211, 219), (200, 222, 234), (176, 85, 42),
              (193, 149, 38), (147, 66, 88), (234, 204, 104), (184, 94, 110), (201, 95, 72), (231, 239, 235), (133, 29, 52), (128, 177, 134)]


def starting_position():
    toby.pu()
    toby.setheading(225)
    toby.fd(250)
    toby.setheading(0)
    toby.pd()


def draw_dots(color_list):
    for _ in range(10):
        for _ in range(10):
            clr = random.choice(color_list)
            size = 20
            toby.dot(size, clr)
            toby.pu()
            toby.fd(50)
            toby.pd()
        toby.pu()
        toby.lt(90)
        toby.fd(50)
        toby.lt(90)
        toby.fd(500)
        toby.setheading(0)
        toby.pd()


starting_position()
draw_dots(color_list)

screen = Screen()
screen.exitonclick()
