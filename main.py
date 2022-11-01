from turtle import Screen
import time

from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard

# set up screen for pong game
screen = Screen()
screen.setup(800, 600)
screen.bgcolor('black')
screen.title('Welcome to pong game')
screen.tracer(0)

r_paddle = Paddle(350)
l_paddle = Paddle(-350)
ball = Ball()
score = ScoreBoard()

# control paddle with key press
screen.listen()
screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down, 'Down')
screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')

is_game_on = True
while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 60 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        score.increase_l_score()

    if ball.xcor() < -380:
        ball.reset_position()
        score.increase_r_score()

screen.exitonclick()
