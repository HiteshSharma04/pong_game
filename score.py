from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("gold")
        self.penup()
        self.hideturtle()
        self.score1 = 0
        self.score2 = 0
        self.goto(-200,250)
        self.write(f"Player A :{self.score1}", align="center" , font=("Courier",20,"bold"))
        self.goto(200,250)
        self.write(f"Player B :{self.score2}", align="center" , font=("Courier",20,"bold"))


    def update(self):
        self.clear()
        self.goto(-200,250)
        self.write(f"Player A :{self.score1}", align="center" , font=("Courier",20,"bold"))
        self.goto(200,250)
        self.write(f"Player B :{self.score2}", align="center" , font=("Courier",20,"bold"))

    def a_score(self):
        self.score1 += 1
        self.update()

    def b_score(self):
        self.score2 += 1
        self.update()

    def game(self):
        self.color("red")
        self.goto(0, 0)
        if self.score1 >= 10:
            self.write(f"GAME OVER !\n Player B WINS!", align="center" , font=("Courier",20,"bold"))
        elif self.score2 >= 10:
            self.write(f"GAME OVER !\n Player A WINS!", align="center" , font=("Courier",20,"bold"))


