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

wn.setup(width=1920, height=1080)
wn.tracer(0)

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Score: 0  High Score :0", align="center", font=("candara", 24, "bold"))

#splash screen, "insert coin/press any button" prompt
#screen switches when button pressed

#set spawn variables to true for n seconds

#spawn barriers
    #2 barriers, one on each side of the screen
    #barriers block all bullets
    #barriers never disappear

#player spawn when variable set to true

#set player hp and damage

    #player starting hp = 
    #player starting damage = 

#set score to 0

#player controlfunctions

#left arrow/A pressed, move left
turtle.listen()
#turtle.onkeypress(move_left, "a")

#right arrow/D pressed, more right
#turtle.onkeypress(move_right, "d")
#space pressed, shoot
#def shoot():
#if player hp hits 0
    #show explosion

    #wait 3 seconds
    
    #go to game start screen


