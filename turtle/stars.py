from turtle import *
from random import *

bgcolor("black")
hideturtle()
speed(0)

width = window_width()
height = window_height()

def draw_star(xpos, ypos):
    size = randrange(4, 10)
    penup()
    goto(xpos, ypos)
    pendown()
    dot(size, "white")

for x in range(100):
    xpos = randrange(round(-width / 2), round(width / 2))
    ypos = randrange(round(-height / 2), round(height / 2))
    draw_star(xpos, ypos)

done()