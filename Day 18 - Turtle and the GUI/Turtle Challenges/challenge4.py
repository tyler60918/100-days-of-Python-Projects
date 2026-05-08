from turtle import Turtle, Screen
import random as r

timmy = Turtle()
timmy.shape("turtle")
timmy.color("palegreen")

timmy.pensize(15)
timmy.speed("fast")

directions = [0, 90, 180, 270]

for _ in range(200):
    timmy.pencolor(r.random(), r.random(), r.random())
    timmy.forward(25)
    timmy.setheading(r.choice(directions))

screen = Screen()
screen.exitonclick()
