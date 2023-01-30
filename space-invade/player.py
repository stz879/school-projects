#listen for variable to be true
wn = turtle.Screen()
#player spawn when variable set to true
player=turtle.Turtle()
player.color("red")
player.penup()
speed=10
wn.onkey(lambda: player.setheading(180), 'Left')
wn.onkey(lambda: player.setheading(0), 'Right')
#set player hp and damage
    #player starting hp = 10
player_hp = 10
    #player starting damage = 1
player_dmg = 1

#set score to 0
score = 0


#player controls
    #left arrow/A pressed, move left
def left():
    player.setheading(180)
    #right arrow/D pressed, more right
def right():
    player.setheading(0)
    #space pressed, shoot

#if player hp hits 0
    #show explosion
    #wait 3 seconds
    #go to game start screen