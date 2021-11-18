from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 280)
        self.color("white")
        self.hideturtle()
        self.increment(0)

    def increment(self, ss):
        self.clear()
        self.write(arg=f"score : {ss}", move=False, align="center", font=("Arial", 10, "normal"))

    def gameover(self):
        self.goto(0, 0)
        self.write(arg=f"GAME OVER", move=False, align="center", font=("Arial", 10, "normal"))
