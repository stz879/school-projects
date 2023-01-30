import turtle
import time
import random
import os

time.sleep(random.randint(1,2))

#draw screen, music begins
wn = turtle.Screen()
wn.title("spase ivaders !!")
wn.bgcolor("purple")
wn.bgpic("spase.gif")

wn.setup(width=1200, height=831)
wn.tracer(0)

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Score: 0  High Score: 0", align="center", font=("candara", 24, "bold"))

#splash screen, "insert coin/press any button" prompt
#screen switches when button pressed

#set spawn variables to true for n seconds

#spawn barriers
    #2 barriers, one on each side of the screen
    #barriers block all bullets
    #barriers never disappear

#player spawn when variable set to true
player = turtle.Turtle()
#set player hp and damage

    #player starting hp = 3
    #player starting damage = 1

#set score to 0

#player controlfunctions
def shoot():
    #function for player shooting
    pass

def move_left():
    #function for player moving left
    pass

def move_right():
    #function for player moving right
    pass


player.listen()
#left arrow/A pressed, move left
turtle.onkeypress(move_left, "a")
turtle.onkeypress(move_left, "Left")

#right arrow/D pressed, move right
turtle.onkeypress(move_right, "d")
turtle.onkeypress(move_right, "Right")

#space pressed, shoot
turtle.onkeypress(shoot, "Space")

#if player hp hits 0
    #show explosion

    #wait 3 seconds
    
    #go to game start screen

wn.mainloop()
