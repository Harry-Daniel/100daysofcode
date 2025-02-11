import random
from turtle import Turtle


START_X=-300
END_X=300
START_Y=-270
END_Y=300
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars=[]
        self.move_distace=STARTING_MOVE_DISTANCE
        self.hideturtle()
        self.start_create_car()
        
            
        

    def start_create_car(self):
        for i in range(15):
            random_x=random.randint(START_X,END_X)
            random_y=random.randint(START_Y,END_Y)
            random_color=random.choice(COLORS)
            new_Car=Turtle('square')
            new_Car.color(random_color)
            new_Car.penup()
            new_Car.goto(x=random_x,y=random_y)
            new_Car.shapesize(stretch_len=2,stretch_wid=1)
            self.cars.append(new_Car)

    def create_new_car(self):
       
        random_y=random.randint(START_Y,END_Y)
        random_color=random.choice(COLORS)
        new_Car=Turtle('square')
        new_Car.color(random_color)
        new_Car.penup()
        new_Car.goto(x=END_X,y=random_y)
        new_Car.shapesize(stretch_len=2,stretch_wid=1)
        self.cars.append(new_Car)

    def move_car(self):
        for car in self.cars:
            car.backward(self.move_distace)
            if car.xcor()<-320:
                self.create_new_car()
                self.cars.remove(car)

    def increase_speed(self):
        self.move_distace+=MOVE_INCREMENT


    