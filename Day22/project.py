from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen=Screen()

r_paddle=Paddle(350)
l_paddle=Paddle(-350)
ball=Ball()
scoreboard= Scoreboard()

screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


screen.listen()
screen.onkey(r_paddle.move_up,"Up")
screen.onkey(r_paddle.move_down,"Down")
screen.onkey(l_paddle.move_up,"w")
screen.onkey(l_paddle.move_down,"s")

game_is_on =True

while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    
    # Detect Collision with wall
    ball.move()
    if ball.ycor()>280:
        ball.direction_y=-1
    elif ball.ycor()<-280:
        ball.direction_y=1

    # Detect collision with r_paddle
    if ball.distance(r_paddle)< 50 and ball.xcor()>320:
        
        ball.direction_x=-1
        ball.increase_speed()
        print(ball.speed())
    elif ball.distance(l_paddle)< 50 and ball.xcor()<-320:
        
        ball.direction_x=1
        ball.increase_speed()
        print(ball.speed())

    if ball.xcor()>380 :
        ball.restart()
        scoreboard.l_point()
    if ball.xcor()<-380:
        ball.restart()
        scoreboard.r_point()
    
    
screen.exitonclick() 