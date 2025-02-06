from turtle import Turtle,Screen
from paddle import Paddle
screen=Screen()

paddle1=Paddle(350)
paddle2=Paddle(-350)


screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


screen.listen()
screen.onkey(paddle1.move_up,"Up")
screen.onkey(paddle1.move_down,"Down")
screen.onkey(paddle2.move_up,"w")
screen.onkey(paddle2.move_down,"s")

game_is_on =True

while game_is_on:
    screen.update()



screen.exitonclick() 