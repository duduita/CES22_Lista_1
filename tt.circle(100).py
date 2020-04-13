from turtle import *

def draw_square(a,color,x,y):
    penup()
    goto(x,y)
    setheading(90)
    backward(a//2)
    setheading(0)
    backward(a//2)
    pendown()
    pencolor(color)
    for _ in range(4):
        forward(a)
        left(90)

draw_square(20,"pink",0,0)
draw_square(40,"pink",0,0)
draw_square(60,"pink",0,0)
draw_square(80,"pink",0,0)
draw_square(100,"pink",0,0)