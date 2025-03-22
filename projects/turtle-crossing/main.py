from turtle import Turtle, Screen
from player import Player
from car_manager import Car
from scoreboard import Scoreboard
import time
import random


POSITION = [-10, -20, -30, -40, -50, 10, 20, 30, 40, 50]

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)

turtle = Player()
car_manager = Car()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(turtle.move_up, "w")
screen.onkey(turtle.move_down, "s")
screen.onkey(turtle.move_left, "a")
screen.onkey(turtle.move_right, "d")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    # detect collision

    for car in car_manager.all_cars:
        if car.distance(turtle) < 20:
            game_is_on = False
            scoreboard.game_over()

    # detect crossing
    if turtle.is_at_finish_line():
        turtle.go_to_start()
        scoreboard.increase_level()

screen.exitonclick()