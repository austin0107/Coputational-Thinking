import turtle
shu = turtle.Turtle()
shu.shape('turtle')
shu.position()
shu.color('purple', 'yellow')
shu.pencolor('black')
shu.turtlesize(6,5,4)
shu.forward(150)
shu.left(90)
shu.forward(150)
shu.penup()
shu.pendown()
shu.hideturtle()
shu.begin_fill()
shu.fillcolor('orange')
shu.circle(250)
shu.circle(250,180,30)
shu.end_fill()
shu.stamp()
shu.write('Turtle Rock')


import turtle
turtle.colormode(250)
pen = turtle.Turtle()
pen.color = (255,215,0)
pen.pensize(10)

for a in range(5):
    pen.forward(250)
    pen.right(144)