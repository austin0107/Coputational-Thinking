import turtle
shelly = turtle.Turtle()
turtle.bgcolor("black")   
for m in range(6):
    shelly.penup()
    shelly.backward(180)
    shelly.right(90)
    shelly.forward(30)
    shelly.left(90)
    shelly.pendown()
    for n in range(6):
        colors = ["red", "green","blue", "gold", "purple","yellow"]
        shelly.color(colors[n]) 
        for i in range(4): 
            shelly.forward(25)
            shelly.left(90)
        shelly.penup() 
        shelly.forward(30)
        shelly.pendown()
shelly.hideturtle()

%Run '簡佑竹Week15-加分2.py'