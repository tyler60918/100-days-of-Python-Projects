from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

game_on = False
user_bet = screen.textinput(
    title="Make your bet", prompt="Which turtle will win the race? Enter a color: "
)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

for i in range(len(colors)):
    turtle = Turtle("turtle")
    turtle.color(colors[i])
    turtle.penup()
    turtle.goto(x=-220, y=(-100 + 40 * i))
    all_turtles.append(turtle)

if user_bet:
    game_on = True

while game_on:
    for turtle in all_turtles:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
        if turtle.xcor() >= 230:
            game_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print(f"You win! The {winning_turtle} turtle is the winner!")
            else:
                print(f"You lose. The {winning_turtle} turtle is the winner.")


screen.exitonclick()
