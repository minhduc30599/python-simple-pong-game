from turtle import Screen, Turtle

from paddle import Paddle

# set up screen for pong game
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Welcome to pong game')
screen.tracer(0)

paddle = Paddle()

# control paddle with key press
screen.listen()
screen.onkey(paddle.go_up, 'Up')
screen.onkey(paddle.go_down, 'Down')

is_game_on = True
while is_game_on:
    screen.update()

screen.exitonclick()