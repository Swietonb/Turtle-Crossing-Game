from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def add_car(self):
        if random.randint(0, 12) % 3 == 0:
            car = Turtle()
            car.penup()
            car.shape("square")
            car.shapesize(stretch_len=2, stretch_wid=1)
            car.color(random.choice(COLORS))
            car.goto(300, random.randint(-260, 260))
            car.setheading(180)
            self.cars.append(car)

    def car_move(self, car):
        car.forward(self.speed)

    def car_increase_speed(self):
        self.speed += MOVE_INCREMENT
