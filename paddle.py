from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_cor):
        super().__init__()
        self.shape('square')
        self.x_cor = x_cor
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x_cor, 0)

    def go_up(self):
        new_y = self.ycor() + 20
        self.speed('fastest')
        self.goto(self.x_cor, new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.speed('fastest')
        self.goto(self.x_cor, new_y)

