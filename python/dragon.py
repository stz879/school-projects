import turtle
#import time
t = turtle
s = t.Screen()

#set screen size, turtle speed, background color, turtle pen/fill color, and turtle shape
s.screensize(600, 600)
t.speed('fastest')
s.bgcolor('white')
t.color('black', 'red')
t.shape('classic')

t.mode('logo')
t.setpos(570, 0)
t.seth(270)
t.pd()
t.forward(50)