from turtle import Turtle
import random
COLORS = ["black", "blue"]  # gives two options for the obstacle colors
MOVE_INCREMENT = 20


class Squares:
    def __init__(self, ):
        self.object = []
        self.Add = 1
        self.STARTING_MOVE_DISTANCE = 5

    def add_square(self):
        for i in range(self.Add):
            color = random.choice(COLORS)       # makes the color of the obstacles random between the array
            y = random.randint(-250, 260)       # makes a random outcome of which position the next obstacle starts at
            object = Turtle()
            object.shape("square")      # sets the shape of the obstacles
            object.shapesize(2, 3)
            object.color(color)
            object.penup()
            object.goto(300, y)
            object.setheading(180)
            self.object.append(object)

    def move(self):
        for object in self.object:
            if object.xcor() < -320:
                object.hideturtle()
                self.object.remove(object)
            else:
                object.forward(self.STARTING_MOVE_DISTANCE)

    def level_up(self):
        self.STARTING_MOVE_DISTANCE += MOVE_INCREMENT
        self.Add += 1

    def reset(self):
        self.STARTING_MOVE_DISTANCE = 10
        self.Add = 1