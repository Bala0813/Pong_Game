from turtle import Turtle
BALL_WIDTH = 1
BALL_HEIGHT = 1

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=BALL_WIDTH, stretch_len=BALL_HEIGHT)
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.1

    def move(self):
        new_x_cor = self.xcor() + self.x_move
        new_y_cor = self.ycor() + self.y_move
        self.goto(new_x_cor, new_y_cor)

    def change_direction_for_wall(self):
        self.y_move *= -1

    def change_direction_for_paddle(self):
        self.x_move *= -1
        self.ball_speed *= 0.9

    def refresh(self):
        self.goto(0, 0)
        self.ball_speed = 0.1
        self.change_direction_for_paddle()
