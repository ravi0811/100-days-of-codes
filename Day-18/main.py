import random
import turtle
from turtle import Turtle,Screen
tim=Turtle()
tim.speed("fastest")

color_list=[(195, 8, 69), (231, 54, 132), (197, 77, 17), (113, 177, 213), (194, 164, 14), (216, 162, 102), (29, 104, 167), (34, 187, 113), (14, 24, 64), (20, 29, 169), (231, 224, 7), (215, 134, 177), (201, 32, 132), (14, 182, 210), (231, 167, 197), (127, 188, 161), (10, 48, 28), (54, 20, 10), (40, 132, 75), (140, 218, 203), (108, 92, 210), (235, 64, 34), (131, 217, 231), (183, 17, 8), (11, 96, 53)]
turtle.colormode(255)

def move_forward():
    for n in range(10):
        tim.pendown()
        tim.dot(20, random.choice(color_list))
        tim.penup()
        tim.forward(50)

tim.penup()

tim.hideturtle()
tim.setheading(225)
tim.forward(250)
tim.setheading(0)
tim.penup()

rows=10
while rows>0:
    move_forward()
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(0)
    rows-=1




screen=Screen()
screen.exitonclick()
