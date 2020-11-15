import turtle
from turtle import Turtle

tl = Turtle()

def draw_fractal(size):
    if size >= 20:
        tl.right(90)
        tl.forward(size*1.73205/2)
        tl.left(150)
        tl.forward(size*3/4)
        tl.left(30)
        tl.forward(size*1.73205/4)
        tl.left(30)
        tl.forward(size*3/4)
        tl.left(150)
        tl.forward(size*1.73205*2/4)
        tl.left(90)
        tl.penup()
        tl.forward(size*3/8)
        tl.pendown()
        draw_fractal(size/1.5)
    else:
        tl.color('yellow')
        tl.forward(size/8)
        tl.begin_fill()
        tl.right(114)
        tl.forward(20)
        tl.left(120)
        tl.forward(20)
        tl.right(48)
        tl.forward(20)
        tl.left(120)
        tl.forward(20)
        tl.right(48)
        tl.forward(20)
        tl.left(120)
        tl.forward(20)
        tl.right(48)
        tl.forward(20)
        tl.left(120)
        tl.forward(20)
        tl.right(48)
        tl.forward(20)
        tl.left(120)
        tl.forward(20)
        tl.end_fill()


size = 300

tl.hideturtle()
tl.penup()
tl.color('green')
tl.goto(0,-size/2)
tl.setheading(90)
tl.pendown()
tl.speed(0)

draw_fractal(size)
turtle.done()
