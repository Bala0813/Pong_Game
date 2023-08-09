from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.updateScore()


    def updateScore(self):
        self.goto(-100, 200)
        self.write(self.left_score, align="center", font=("arial", 60, "normal"))
        self.goto(100, 200)
        self.write(self.right_score, align="center", font=("arial", 60, "normal"))


    def left_increment(self):
        self.left_score += 1
        self.clear()
        self.updateScore()

    def right_increment(self):
        self.right_score += 1
        self.clear()
        self.updateScore()

    def gameover(self, winner):
        self.goto(0, 0)
        self.write(f"Game Over!, the winner is {winner}", move=False, align="center", font=("arial", 20, "normal"))


