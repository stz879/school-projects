#listen for variable to be true
#player spawn when variable set to true
player = turtle.Turtle()
player.shape("player.gif")
player.penup()

#set player hp and damage
    #player starting hp = 10
player_hp = 10
    #player starting damage = 1
player_dmg = 1

#set score to 0
score = 0
player.speed(0)
playerspeed = 15


#player controls
    #left arrow/A pressed, move left
    #right arrow/D pressed, more right
    #space pressed, shoot
player.setposition(0,-250)
player.setheading(90)

#if player hp hits 0
    #show explosion
    #wait 3 seconds
    #go to game start screen
    player = turtle.Turtle()
