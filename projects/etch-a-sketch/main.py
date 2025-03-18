# PYTHON HIDER ORDER FUNCTIONS AND EVENT LISTENERS

import turtle as t
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def rotate_left():
    tim.left(10)

def rotate_right():
    tim.right(10)

def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()

# HIGHER ORDER FUNCTION: take one or more functions as arguments
screen.onkey(key="d", fun=move_forwards)
screen.onkey(key="a", fun=move_backwards)
screen.onkey(key="c", fun=rotate_right)
screen.onkey(key="z", fun=rotate_left)
screen.onkey(clear_screen, "p")
screen.exitonclick()