from turtle import Turtle


STARTING_POSITION = (0, -270)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
    
    def move_up(self):
        self.forward(MOVE_DISTANCE)
        


# from turtle import Turtle
# class Paddle(Turtle):
#     def __init__(self,xcor):
#         super().__init__()
#         self.shape("square")
#         self.penup()
        
#         self.color("white")
#         self.shapesize(stretch_len=5,stretch_wid=1)
#         self.goto(x=xcor,y=0)
#         self.setheading(90)

    
#     def move_down(self):
#         self.backward(20)