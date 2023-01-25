import turtle
t = turtle
s = t.Screen()

#set screen size, turtle speed, background color, turtle pen/fill color, and turtle shape
s.screensize(800, 800)
t.speed('normal')
s.bgcolor('white')
t.pencolor("black")
t.fillcolor("red")
t.shape('classic')

t.mode('logo')
t.showturtle
t.pu()
t.setpos(200, 0)
t.seth(270)
t.pd()
t.forward(100)
t.pu()
t.forward(20)
t.pd()
t.begin_fill()
t.forward(40)
t.left(90)
t.forward(40)
t.seth(45)
t.forward(55)
t.end_fill()

