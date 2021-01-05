import turtle
shelly=turtle.Turtle()
turtle.bgcolor('black')
shelly.pencolor('white')
for i in range(36):
    shelly.penup()
    shelly.forward(200)
    for j in range(6):
        colors=["red","yellow","purple","gold","green","white"]
        shelly.color(colors[j])
        shelly.pendown()
        shelly.circle(10-j)
        shelly.penup()
        shelly.backward(20)
    shelly.backward(80) 
    shelly.right(10)
shelly.hideturtle()

%Run '簡佑竹Week15-加分1.py'