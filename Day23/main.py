import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


player=Player()
car=CarManager()
scoreboard=Scoreboard()
screen.listen()
screen.onkey(player.move_up,"Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.move_car()
    if player.ycor()>=280:
        car.increase_speed()
        print(car.move_distace)
        player.goto(0,-280)
        scoreboard.level+=1
        scoreboard.update_scoreboard()
    
    for single_car in car.cars:
        if single_car.distance(player)< 20:
            game_is_on=False

scoreboard.game_over()




screen.exitonclick()