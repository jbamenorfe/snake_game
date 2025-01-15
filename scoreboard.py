from turtle import Turtle
ALIGNMENT = ("center")
FONT = ("Courier", 16, "normal")
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highest_score = self.get_score_data()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.update_scoreboard()

    def get_score_data(self):
        with open("data.txt") as file:
            contents = int(file.read())
            return contents

    def save_score_data(self):
        with open("data.txt", mode="w") as file:
            file.write(str(self.highest_score))

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} |<**>| Highest Score: {self.highest_score}", move=False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
