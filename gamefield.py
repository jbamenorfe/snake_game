from turtle import Turtle
STARTING_X = -290
STARTING_Y = -280
FIELD_COLOR = "blue"

class GameField(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color(FIELD_COLOR)
        self.goto(STARTING_X, STARTING_Y)
        self.draw_field()

    def draw_field(self):
        self.pendown()
        self.hideturtle()
        self.pensize(5)
        self.forward(570)
        self.left(90)
        self.forward(530)
        self.left(90)
        self.forward(570)
        self.left(90)
        self.forward(530)

