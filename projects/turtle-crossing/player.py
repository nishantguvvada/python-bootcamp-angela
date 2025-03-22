from turtle import Turtle

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.goto(0, -270)

    def move_up(self):
        self.forward(10)
    
    def move_down(self):
        self.backward(10)

    def move_left(self):
        x_cor = self.xcor()
        y_cor = self.ycor()
        self.goto(x_cor - 10, y_cor)

    def move_right(self):
        x_cor = self.xcor()
        y_cor = self.ycor()
        self.goto(x_cor + 10, y_cor)

    def go_to_start(self):
        self.goto(0, -270)
    
    def is_at_finish_line(self):
        if self.ycor() > 280:
            return True
        else:
            return False 