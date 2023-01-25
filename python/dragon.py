import turtle
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
t.pu()
t.forward(10)
t.pd()
t.forward(30)
t.left(90)
t.forward(20)
t.seth(315)
t.forward(40)