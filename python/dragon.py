import turtle
t = turtle
s = t.Screen()

#turtle settings
t.mode('logo')
t.hideturtle()
s.screensize(800, 800)
t.speed('fastest')
s.bgcolor('white')
t.pencolor('black')
t.fillcolor('red')
t.shape('classic')

n = 1

while n == 1:
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
  t.seth(316)
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
  t.seth(44)
  t.forward(57)
  t.end_fill()

  t.pu()
  t.seth(270)
  t.forward(14)

  #fourth triangle
  t.pd()
  t.begin_fill()
  t.forward(91)
  t.seth(120)
  t.forward(70)
  t.seth(42)
  t.forward(48)
  t.end_fill()

  t.up()
  t.setposition(-10, -130)
  t.seth(20)
  t.width(width=9)
  t.down()

  #tail
  t.begin_fill()
  t.seth(-160)
  t.forward(5)
  t.seth(-340)
  t.forward(20)
  t.seth(-200)
  t.forward(20)
  t.seth(-90)
  t.forward(5)
  t.end_fill()

  t.seth(0)

  #body
  t.circle(-20, 360/11)
  t.width(width=8)
  t.circle(80, 360/6)
  t.width(width=11)
  t.circle(-80, 360/8)
  t.width(width=13)
  t.circle(-80,360/10)
  t.width(width=10)
  t.circle(80,360/8)

  #head
  t.begin_fill()
  t.seth(90)
  t.forward(20)
  t.seth(340)
  t.forward(60)
  t.seth(200)
  t.forward(60)
  t.seth(90)
  t.forward(20)
  t.end_fill()
  
  n = 0
  break
  
#close window if clicked
t.exitonclick()
