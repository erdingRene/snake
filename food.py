from turtle import Turtle
import random as rd


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = rd.randint(-280, 280)
        random_y = rd.randint(-280, 280)
        self.goto(random_x, random_y)
