from turtle import Turtle, Screen
import random as r

timmy = Turtle()
timmy.shape("turtle")
timmy.color("palegreen")
timmy.speed("fastest")


def draw_spirograph(gap):
    for _ in range(int(360 / gap)):
        timmy.pencolor(r.random(), r.random(), r.random())
        timmy.circle(100)
        timmy.right(gap)


draw_spirograph(10)

screen = Screen()
screen.exitonclick()
