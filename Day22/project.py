from turtle import Turtle,Screen

screen=Screen()
paddle1=Turtle("square")
paddle1.penup()
paddle1.color("white")
paddle1.shapesize(stretch_len=5,stretch_wid=1)
paddle1.goto(x=350,y=0)
paddle1.setheading(90)





screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong")

def move_up():
    paddle1.forward(20)

def move_down():
    paddle1.backward(20)

screen.listen()
screen.onkey(move_up,"Up")
screen.onkey(move_down,"Down")



screen.exitonclick()