from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.shapesize(stretch_len=1,stretch_wid=1)
        self.penup()
        self.x_m = 10
        self.y_m = 10
        self.mv_speed = 0.1

    def move(self):
        x1 = self.xcor() + self.x_m
        y1 = self.ycor() + self.y_m
        self.goto(x1,y1)

    def bounce_y(self):
        self.y_m *= -1


    def bounce_x(self):
        self.x_m *= -1  
        self.mv_speed *= 0.9


    def reset(self):
        self.goto(0, 0)
        self.mv_speed = 0.1
        self.bounce_x()  
