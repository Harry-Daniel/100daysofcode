from turtle import Turtle
class Paddle(Turtle):
    def __init__(self,xcor):
        super().__init__()
        self.shape("square")
        self.penup()
        
        self.color("white")
        self.shapesize(stretch_len=5,stretch_wid=1)
        self.goto(x=xcor,y=0)
        self.setheading(90)

    def move_up(self):
        self.forward(20)

    def move_down(self):
        self.backward(20)