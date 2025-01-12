from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.penup()
        self.color("green")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-270, 250)
        random_y = random.randint(-260, 235)
        self.goto(random_x, random_y)
