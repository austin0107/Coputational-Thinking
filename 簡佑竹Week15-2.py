# 方法(一):巢狀迴圈
import turtle
austin=turtle.Turtle()
for i in range(6): # 外迴圈重複正方形6次
    for j in range(4): #內迴圈重複4次來畫正方形
        austin.forward(150)
        austin.left(90)
    austin.right(60) #畫下一個正方形前轉彎

# 方法(二):巢狀迴圈 + 加上色彩
colors = ["red","orange","yellow","green","blue", "purple"]
for n in range(6):
    austin.color(colors[n])
    for j in range(4): 
        austin.forward(150)
        austin.left(90)
    austin.right(60)

# 方法(三) :巢狀迴圈 + 填滿色彩
colors = ["red","orange","yellow","green","blue", "purple"]
for n in range(6):
    austin.color(colors[n])
    austin.begin_fill()
    austin.fillcolor(colors[n])
    for j in range(4):
        austin.forward(150)
        austin.left(90)
    austin.right(60)
    austin.end_fill()   