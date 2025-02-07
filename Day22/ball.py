from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup() 
        self.color("white")
        self.start_direction_x=1
        self.direction_y=-1
        self.direction_x=1
        self.move_speed =0.1
        

    def move(self):
        new_x=self.xcor()+(10*self.direction_x)
        new_y=self.ycor()+(10*self.direction_y)
        self.goto(x=new_x,y=new_y)
        
      
    def restart(self):
        self.goto(0,0)
        self.start_direction_x*=-1
        self.move_speed=0.1
        self.direction_x=self.start_direction_x


    def increase_speed(self):
        self.move_speed*=0.9
        