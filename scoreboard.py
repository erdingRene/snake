from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.counter = 0
        self.goto(0, 250)
        self.hideturtle()

    def count(self):
        self.counter += 1

    def writer(self):
        self.write(f'Score: {self.counter}', align=ALIGNMENT, font=FONT)

    def change_score(self):
        self.count()
        self.clear()
        self.writer()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)
