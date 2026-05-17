import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def add_car(self):
        """Adds a new random car to the right side of screen"""
        if random.randint(1, 6) == 1:
            new_car = Turtle()
            new_car.color(random.choice(COLORS))
            new_car.shape("square")
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            car_y = random.randint(-250, 250)
            new_car.goto(300, car_y)
            self.cars.append(new_car)

    def move_cars(self):
        """Moves all cars to the left"""
        for car in self.cars:
            car.goto(car.xcor() - self.car_speed, car.ycor())
            if car.xcor() < -320:
                self.cars.remove(car)

    def new_level(self):
        """Increases the movement speed for the cars"""
        self.car_speed += MOVE_INCREMENT
