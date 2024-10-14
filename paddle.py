from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,a):
        super().__init__()
        self.shape("square")
        self.color("green")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.goto(a)

    def up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def down(self):
        self.goto(self.xcor(), self.ycor() - 20)