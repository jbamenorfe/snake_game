from turtle import Turtle
ALIGNMENT = ("center")
FONT = ("Courier", 24, "normal")
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 260)
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"SCORE: {self.score}", move=False, align=ALIGNMENT, font=FONT)
        self.score += 1

    def game_over(self) -> object:
        self.goto(0,0)
        self.write("GAME OVER!", move=False, align=ALIGNMENT, font=FONT)
