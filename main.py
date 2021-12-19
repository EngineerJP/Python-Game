# Crossy Road Project COM302 Python Programming
import time
from tkinter import messagebox
from turtle import Screen
from player import Player           # import the Player() class from player.py
from playertwo import PlayerTwo     # import the PlayerTwo() class from playertwo.py
from obstacles import Squares       # import Squares() class from obstacles.py

screen = Screen()
screen.title("TAKE A RIDE (Crossy Road Game)")      # Puts a title at the top of the screen
screen.setup(width=600, height=600)
screen.bgcolor('Green')
screen.tracer(0)
player = Player()
screen.listen()
# Code for when you press a key in the game to move player one is w,a,s,d
screen.onkey(key="w", fun=player.move_up)
screen.onkey(key="a", fun=player.move_left)
screen.onkey(key="d", fun=player.move_right)
screen.onkey(key="s", fun=player.move_down)
playertwo = PlayerTwo()
# Code for when you press a key in the game to move player two is i,j,l,k
screen.onkey(key="i", fun=playertwo.move_up_two)
screen.onkey(key="j", fun=playertwo.move_left_two)
screen.onkey(key="l", fun=playertwo.move_right_two)
screen.onkey(key="k", fun=playertwo.move_down_two)


object = Squares()
game_is_on = True
a = 0
while game_is_on:
    time.sleep(.1)
    object.move()
    for object_ in object.object:
        if object_.distance(player, playertwo) < 22:
            if not messagebox.askyesno("Game Over!", "Do you want to play again?"):
                game_is_on = False
            else:
                object.reset()
                player.reset_position()
                playertwo.reset_position()
# Resets the position of the character when goes above the top of the screen
    if player.ycor() > 280:
        player.reset_position()
        object.level_up()
    if playertwo.ycor() > 280:
        playertwo.reset_position()
        object.level_up()
    if a % 5 == 0:
        object.add_square()
    screen.update()
    a += 0.5    # increases the speed that the objects come from the right to the left of screen
screen.exitonclick()