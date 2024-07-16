from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("black")
        self.hideturtle()
        self.speed("fastest")
        self.goto(-280, 260)
        self.level = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Level: {self.level}", font=FONT)

    def add_score(self):
        self.level += 1
        self.update_score()

    def game_over(self):
        self.color("red")
        self.goto(-80, 0)
        self.write("Game Over", font=FONT)