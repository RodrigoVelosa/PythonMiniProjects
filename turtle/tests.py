from turtle import *
from random import *

def create_square():
    forward(50)
    right(90)
    forward(50)
    right(90)
    forward(50)
    right(90)
    forward(50)


def create_circle():
    color("green")
    begin_fill()
    circle(50)
    end_fill()
    color("black")
    penup()
    forward(100)
    pendown()
    color("#FFDD00")
    begin_fill()
    circle(50)
    end_fill()

def filled_square():
    color("blue")
    begin_fill()
    create_square()
    end_fill()

def create_equilateral_triangle():
    forward(100)
    left(120)
    forward(100)
    left(120)
    forward(100)

def solar_system():
    bgcolor("black")

    color("orange")
    begin_fill()
    circle(60)
    end_fill()

    penup()
    forward(100)
    pendown()

    color("grey")
    begin_fill()
    circle(20)
    end_fill()

    penup()
    forward(80)
    pendown()

    color("red")
    begin_fill()
    circle(40)
    end_fill()

    penup()
    forward(90)
    pendown()

    color("green")
    begin_fill()
    circle(40)
    end_fill()

def randomness():
    forward(randrange(20, 100))
    right(randrange(0, 360))
    forward(randrange(20, 100))

randomness()

done()