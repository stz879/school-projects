import turtle
t = turtle
s = t.Screen()

#turtle settings
t.mode('logo')
t.hideturtle()
s.screensize(800, 800)
t.speed('normal')
s.bgcolor('white')
t.pencolor("black")
t.fillcolor("red")
t.shape('classic')

#right wing
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
t.forward(58)
t.end_fill()
t.pu()
t.forward(15)



t.exitonclick()