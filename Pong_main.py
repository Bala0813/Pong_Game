from turtle import Screen
from Pong_paddle import Paddle
from Pong_Ball import Ball
from Pong_Scoreboard import Score
import time
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

right_paddle = Paddle(350, 0)
left_paddle = Paddle(-350, 0)

ball = Ball()
score = Score()

screen.listen()
# Keyboard Controls
screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")
screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()
    # Top boundary collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.change_direction_for_wall()
    # Paddle collision
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.change_direction_for_paddle()
    # score calculation
    if ball.xcor() > 380:
        ball.refresh()
        score.left_increment()
    if ball.xcor() < -380:
        ball.refresh()
        score.right_increment()

    if score.left_score == 5:
        game_is_on = False
        score.gameover("Right_Side")

    if score.right_score == 5:
        game_is_on = False
        score.gameover("Left_Side")

screen.exitonclick()