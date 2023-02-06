import turtle
t = turtle
s = t.Screen()

#turtle settings
t.mode('logo')
t.hideturtle()
s.screensize(800, 800)
t.speed('fast')
s.bgcolor('white')
t.pencolor('black')
t.fillcolor('red')
t.shape('classic')



#right wing
t.pu()
t.setpos(80, 0)
t.seth(270)

#first triangle
t.pd()
t.begin_fill()
t.forward(40)
t.seth(180)
t.forward(40)
t.seth(45)
t.forward(58)
t.end_fill()

t.pu()
t.forward(13)
t.seth(180)
t.forward(15)

#second triangle
t.pd()
t.begin_fill()
t.forward(50)
t.seth(285)
t.forward(40)
t.seth(44)
t.forward(55)
t.end_fill()

t.pu()
t.forward(15)
t.seth(180)
t.forward(10)

#third triangle
t.pd()
t.begin_fill()
t.forward(50)
t.seth(75)
t.forward(40)
t.seth(316)
t.forward(57)
t.end_fill()

t.pu()
t.seth(90)
t.forward(15)

#fourth triangle
t.pd()
t.begin_fill()
t.forward(90)
t.seth(240)
t.forward(70)
t.seth(319)
t.forward(48)
t.end_fill()


#left wing
t.pu()
t.setpos(-80, 0)
t.seth(90)

#first triangle
t.pd()
t.begin_fill()
t.forward(40)
t.seth(180)
t.forward(40)
t.seth(315)
t.forward(58)
t.end_fill()

t.pu()
t.forward(13)
t.seth(180)
t.forward(15)

#second triangle
t.pd()
t.begin_fill()
t.forward(50)
t.seth(75)
t.forward(40)
t.seth(314)
t.forward(55)
t.end_fill()

t.pu()
t.forward(15)
t.seth(180)
t.forward(10)

#third triangle
t.pd()
t.begin_fill()
t.forward(50)
t.seth(285)
t.forward(40)
t.seth(46)
t.forward(57)
t.end_fill()

t.pu()
t.seth(270)
t.forward(15)

#fourth triangle
t.pd()
t.begin_fill()
t.forward(90)
t.seth(120)
t.forward(70)
t.seth(49)
t.forward(48)
t.end_fill()

#close window if clicked
t.exitonclick()
