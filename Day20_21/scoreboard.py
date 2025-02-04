from turtle import Turtle
ALIGNMENT = 'center'
FONT = ("Courier",24,"normal")

class Scoreboard(Turtle):
    
    def __init__(self):
        self.score=0
        super().__init__()
        self.goto(0,250)
        self.color("white")
        self.hideturtle()
        self.refresh()

    def refresh(self):
        self.clear()
        self.write(f"Score = {self.score}",False,ALIGNMENT,FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align=ALIGNMENT,font=FONT)

    def increase_score(self):
        self.score+=1
        self.refresh()