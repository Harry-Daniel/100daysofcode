from turtle import Screen,Turtle

screen= Screen()

screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My snake game")

position=0
for tim in range (3):
    tim=Turtle('square')
    tim.color("white")
    tim.backward(position)
    position+=20




screen.exitonclick()