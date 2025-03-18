import turtle as t
from turtle import Turtle, Screen



screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
is_race_on = False
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_racers = []

space = 0
for color in colors:
    racer = Turtle(shape="turtle")
    racer.color(f"{color}")
    racer.penup()
    racer.goto(x=-200, y=-50+space)
    space += 30
    all_racers.append(racer)

import random

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_racers:
        if turtle.xcor() > 230:
            winning_racer = turtle.pencolor()
            if winning_racer == user_bet:
                print(f"You've won! The {winning_racer} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_racer} turtle is the winner!")
            is_race_on = False
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()