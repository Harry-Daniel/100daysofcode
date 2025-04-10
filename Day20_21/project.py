from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard
screen= Screen()

screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

snake=Snake()
food=Food()
scoreboard=Scoreboard()



screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")



game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    
    # Detect collision from food
    if snake.head.distance(food)<15:
        scoreboard.increase_score()
        food.refresh()
        snake.extend()

    # Detect collision with wall
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        scoreboard.reset()
        snake.reset()
        

    # Detect Collision with tail
    for segment in snake.segments[1:]:
       if snake.head.distance(segment)<10:
            scoreboard.reset()
            snake.reset()
           
    # if head collides with any segment in tail
screen.exitonclick()