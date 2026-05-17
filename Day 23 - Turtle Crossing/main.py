import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.onkey(player.move, "Up")

game_is_on = True
game_loop_num = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()
    game_loop_num += 1
    car_manager.add_car()
    car_manager.move_cars()

    # Detect collision with car
    for car in car_manager.cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect player successfully made it to far wall
    if player.check_goal():
        scoreboard.new_level()
        car_manager.new_level()

screen.exitonclick()
