import colorgram

colors = colorgram.extract('image.jpg', 6)

color_schema = [(color.rgb.r, color.rgb.g, color.rgb.b) for color in colors]

from turtle import Turtle, Screen
import turtle as t
import random

t.colormode(255)
tim = Turtle()
tim.penup()
tim.speed("fastest")
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100



for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_schema))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = Screen()
screen.exitonclick()