from turtle import Turtle
PADDLE_WIDTH = 5
PADDLE_HEIGHT = 1
MOVEMENT_DISTANCE = 20

class Paddle(Turtle):
    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.paddle_x_cor = x_cor
        self.paddle_y_cor = y_cor
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=PADDLE_WIDTH, stretch_len=PADDLE_HEIGHT)
        self.penup()
        self.goto(self.paddle_x_cor, self.paddle_y_cor)


    def move_up(self):
        cur_y_cor = self.ycor() + MOVEMENT_DISTANCE
        self.goto(self.xcor(), cur_y_cor)

    def move_down(self):
        cur_y_cor = self.ycor() - MOVEMENT_DISTANCE
        self.goto(self.xcor(), cur_y_cor)
