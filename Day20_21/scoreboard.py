from turtle import Turtle
ALIGNMENT = 'center'
FONT = ("Courier",24,"normal")

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score=0
        self.high_score=0
        self.goto(0,250)
        self.color("white")
        self.hideturtle()
        self.refresh()

    def refresh(self):
        self.clear()
        self.write(f"Score = {self.score} High Score: {self.high_score}",align=ALIGNMENT,font=FONT)

 
    def reset(self):
        if self.score>self.high_score:
            self.high_score = self.score
        self.score=0
        self.refresh()
 
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER",align=ALIGNMENT,font=FONT)

    def increase_score(self):
        self.score+=1
        self.refresh()