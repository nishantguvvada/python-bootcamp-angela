from turtle import Turtle, Screen
import turtle as t
import random

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")

t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


fd = timmy_the_turtle.forward
rt = timmy_the_turtle.right
lt = timmy_the_turtle.left
up = timmy_the_turtle.penup
dw = timmy_the_turtle.pendown
sz = timmy_the_turtle.pensize

# for _ in range(50):
#     fd(10)
#     up()
#     fd(10)
#     dw()

# def calculate_angle(sides: int):
#     angle = 360 / sides
#     return angle

# for i in range(3, 10):
#     for j in range(0, i):
#         fd(100)
#         rt(calculate_angle(i))


direction = [0, 90, 180, 270]
timmy_the_turtle.speed("fastest")

# for _ in range(200):
#     timmy_the_turtle.color(random_color())
#     fd(20)
#     timmy_the_turtle.setheading(random.choice(direction))

def draw_spirograph(size):
    for _ in range(360 // size):
        timmy_the_turtle.color(random_color())
        timmy_the_turtle.circle(100)
        current_heading = timmy_the_turtle.heading()
        timmy_the_turtle.setheading(current_heading + size)

draw_spirograph(5)

screen = Screen()
screen.exitonclick()