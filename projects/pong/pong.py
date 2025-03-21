from turtle import Turtle, Screen
import turtle as t
from resources import Paddle, Ball, Score
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

player_1 = Paddle((350, 0))
player_2 = Paddle((-350, 0))

ball = Ball()

score = Score()

screen.listen()
screen.onkey(player_1.up, "Up")
screen.onkey(player_1.down, "Down")

screen.onkey(player_2.up, "w")
screen.onkey(player_2.down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    score.update_score()

    # Detect wall collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect paddle collision
    if ball.distance(player_1.paddle) < 50 and ball.xcor() > 320 or ball.distance(player_2.paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect player 1 miss
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()

    # Detect player 1 miss
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()

screen.exitonclick()