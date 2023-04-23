import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


def main():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.tracer(0)

    scoreboard = Scoreboard()
    player = Player()
    car_manager = CarManager()

    screen.listen()
    screen.onkey(player.move, "w")

    game_is_on = True
    while game_is_on:
        time.sleep(0.1)
        screen.update()

        # Detecting if player ended the level
        if player.level_finished():
            player.starting_position()
            scoreboard.level_up()
            car_manager.car_increase_speed()
        # Generating cars
        car_manager.add_car()
        for car in car_manager.cars:
            car_manager.car_move(car)
        # Detecting if player hits the car
            if player.distance(car) < 20:
                game_is_on = False
                scoreboard.game_over()
    screen.exitonclick()


if __name__ == "__main__":
    main()