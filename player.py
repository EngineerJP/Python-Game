from turtle import Turtle
import random
STARTING_POSITION = (-100, -280)    # Creates the starting position for the player one character at -100 on the x axis
x = random.randint(-250, 260)
FINISH_LINE_Y = 280 # The finish line before reset is at the top of the screen


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.reset_position()

    def reset_position(self):
        self.shape("turtle")    # sets the shape of the character throughout the library options
        self.setheading(90)     # starts the degrees of the character up 90 degrees
        self.penup()
        self.goto(STARTING_POSITION)

# these functions allows the character to change its direction and move in that direction with one motion
    def move_up(turtle):
        turtle.setheading(90)
        turtle.forward(10)

    def move_right(turtle):
        turtle.setheading(0)
        turtle.forward(10)

    def move_left(turtle):
        turtle.setheading(180)
        turtle.forward(10)

    def move_down(turtle):
        turtle.setheading(270)
        turtle.forward(10)


