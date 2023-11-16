from turtle import Turtle, Screen, colormode
from random import randint, choice


toby = Turtle()
toby.shape("turtle")
toby.color('Green')
toby.pensize(2)
toby.speed("fastest")
colormode = colormode(255)


def draw_circle(radius, angle):
    clr = (randint(0, 255),
           randint(0, 255), randint(0, 255))
    toby.color(clr)
    toby.circle(radius)
    toby.setheading(angle)


i = 0
while i < 360:
    draw_circle(radius=100, angle=float(i))
    i += 5

screen = Screen()
screen.exitonclick()
