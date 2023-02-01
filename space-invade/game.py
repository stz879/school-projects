import turtle
import time
import random
import os
import winsound

wn = turtle.Screen()
wn.register_shape("spaceship.gif")

#draw screen, music begins
wn.title("spase ivaders !!")
wn.bgcolor("#db5ef7")
wn.bgpic("spase.gif")
wn.setup(width=1200, height=831)
wn.tracer(0)


def game():
    #set score to 0
    score = 0
    high_score = 0

    pen = turtle.Turtle()
    pen.speed(0)
    pen.hideturtle()
    pen.color("white")
    pen.goto(-200, 330)
    pen.write(f"Score: {score}", align="center", font=("Comic Sans MS", 24, "bold"))
    pen.goto(200, 330)
    pen.write(f"High Score: {high_score}", align="center", font=("Comic Sans MS", 24, "bold"))

    #splash screen, "insert coin/press any button" prompt
    #screen switches when button pressed

    #spawn barriers
        #2 barriers, one on each side of the screen
        #barriers block all bullets
        #barriers never disappear

    #player spawn
    player = turtle.Turtle()
    turtle.mode("logo")
    player.speed("slowest")
    player.shape("circle")
    player.pencolor("black")
    player.penup()
    player.resizemode("user")
    player.shapesize(50, 50, 5)
    player.showturtle()
    player.goto(0, -300)
    player.seth(0)

    #set player hp
    player_hp = 3
        

    #player control functions
    def shoot():
        #function for player shooting
        pass

    def move_left():
        player.seth(270)
        player.backward(5)

    def move_right():
        player.seth(90)
        player.forward(5)


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
