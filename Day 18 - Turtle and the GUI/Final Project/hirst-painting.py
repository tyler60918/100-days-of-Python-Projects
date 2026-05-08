from turtle import Turtle, Screen
import random

turtle = Turtle()
turtle.speed("fastest")
turtle.hideturtle()
turtle.penup()
screen = Screen()
screen.colormode(255)

# Got from my color-extractor.py file
colors = [
    (242, 117, 31),
    (240, 79, 94),
    (240, 95, 34),
    (154, 113, 8),
    (128, 215, 206),
    (212, 153, 163),
    (150, 186, 224),
    (167, 45, 137),
    (51, 91, 86),
    (85, 183, 4),
    (29, 37, 42),
    (132, 218, 221),
    (249, 207, 0),
    (240, 231, 235),
    (227, 237, 233),
]

turtle.teleport(-250, -250)

for i in range(10):
    turtle.teleport(-250, -250 + 50 * i)
    for _ in range(10):
        turtle.dot(20, random.choice(colors))
        turtle.forward(50)

screen.exitonclick()
