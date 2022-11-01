from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.paddle = Turtle(shape='square')
        self.create_paddle()

    def create_paddle(self):
        self.paddle.color('white')
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle.penup()
        self.paddle.goto(350, 0)

    def go_up(self):
        new_y = self.paddle.ycor() + 20
        self.paddle.goto(350, new_y)

    def go_down(self):
        new_y = self.paddle.ycor() - 20
        self.paddle.goto(350, new_y)
