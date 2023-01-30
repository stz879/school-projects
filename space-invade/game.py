import turtle
import time
import random
import os
import winsound

wn = turtle.Screen()

def game():
    time.sleep(random.randint(1,2))

    #draw screen, music begins
    
    wn.title("spase ivaders !!")
    wn.bgcolor("#db5ef7")
    wn.bgpic("spase.gif")

    wn.setup(width=1200, height=831)
    wn.tracer(0)

    pen = turtle.Turtle()
    pen.speed(0)
    pen.hideturtle()
    pen.color("white")
    pen.goto(-200, 330)
    pen.write("Score: 0", align="center", font=("candara", 24, "bold"))
    pen.goto(200, 330)
    pen.write("High Score: 0", align="center", font=("candara", 24, "bold"))

    #splash screen, "insert coin/press any button" prompt
    #screen switches when button pressed

    #set spawn variables to true for n seconds

    #spawn barriers
        #2 barriers, one on each side of the screen
        #barriers block all bullets
        #barriers never disappear

    #player spawn when variable set to true
    #player = turtle.Turtle()

    #set player hp and damage
    player_hp = 3
        #player starting hp = 3
    #player_dmg = 1
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


    wn.listen()
    #left arrow/A pressed, move left
    turtle.onkeypress(move_left, "a")
    turtle.onkeypress(move_left, "Left")

    #right arrow/D pressed, move right
    turtle.onkeypress(move_right, "d")
    turtle.onkeypress(move_right, "Right")

    #space pressed, shoot
    turtle.onkeypress(shoot, "space")

    #if player hp hits 0
    if player_hp == 0:
        #show explosion
        wn.bgpic("explosion-boom.gif")
        #wait 1 second
        time.sleep(1)
        #go to game start screen
        game()

game()
wn.mainloop()

