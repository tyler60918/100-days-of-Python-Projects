from turtle import Turtle, Screen
import random as r

timmy = Turtle()
timmy.shape("turtle")
timmy.color("palegreen")

for sides in range(3, 11):
    angle = 360 / sides
    color = (r.random(), r.random(), r.random())
    timmy.pencolor(color)
    for _ in range(sides):
        timmy.forward(100)
        timmy.right(angle)

screen = Screen()
screen.exitonclick()
