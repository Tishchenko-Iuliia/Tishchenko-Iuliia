import turtle
from turtle import Turtle

tl = Turtle()

size = 250


def draw_fractal(size):
    if size >= 10:
        tl.forward(size)
        draw_fractal(size/2)
        tl.left(60)
        draw_fractal(size/2)
        tl.left(60)
        draw_fractal(size/2)
        tl.left(120)
        draw_fractal(size/2)
        tl.left(60)
        draw_fractal(size/2)
        tl.left(60)
        tl.penup()
        tl.backward(size)
        tl.pendown()

    else:
        tl.circle(4)


tl.penup()
tl.color('blue')
tl.goto(0, -size)
tl.setheading(90)
tl.pendown()
turtle.tracer(0, 0)
tl.speed(0)

draw_fractal(size)
turtle.done()
