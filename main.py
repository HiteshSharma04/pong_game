from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from score import Score
screen = Screen()
screen.bgcolor("black")
screen.setup(width=900, height=600)
screen.title("PONG")
screen.tracer(0)
screen.listen()




r_paddle = Paddle((410,0))
l_paddle = Paddle((-410,0))
ball = Ball()
score = Score()

screen.onkey(r_paddle.up,"Up")
screen.onkey(r_paddle.down,"Down")
screen.onkey(l_paddle.up,"w")
screen.onkey(l_paddle.down,"s")


game = True
while game:
    time.sleep(ball.mv_speed)
    screen.update()
    ball.move()

    if ball.ycor() < -280 or ball.ycor() > 280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 380 or  ball.distance(l_paddle) < 50 and ball.xcor() < -380 :
        ball.bounce_x()

    if ball.xcor() > 430:
        ball.reset()
        score.a_score()
    
    if ball.xcor() < -440:
        ball.reset()
        score.b_score()

    if score.score1 >= 10 or score.score2 >= 10:
        score.game()
        game = False


screen.exitonclick() 