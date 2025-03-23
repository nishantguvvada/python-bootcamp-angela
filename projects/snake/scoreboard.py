from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.get_high_score()
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.write(f"Score : {self.score} High Score: {self.high_score}", align="center", font=("Arial", 24, "normal"))
        self.hideturtle()
        
    def get_high_score(self):
        with open("data.txt", "r") as value:
            return int(value.read())
        
    def set_high_score(self):
        with open("data.txt", "w") as value:
            value.write(f"{self.high_score}")

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score : {self.score} High Score: {self.high_score}", align="center", font=("Arial", 24, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.set_high_score()
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"Game Over", align="center", font=("Arial", 24, "normal"))
    
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()