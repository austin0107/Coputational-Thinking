# 方法(一):for 迴圈
import turtle
austin=turtle.Turtle()
for s in range(4):
    austin.forward(300)
    austin.right(90)

# 方法(二):for 迴圈 + 色彩(紫色)
austin.color('blue')
for s in range(4):
    austin.forward(300)
    austin.right(90)

# 方法(三):for 迴圈 + 塗滿色彩(黃色)
austin.begin_fill()
austin.fillcolor('yellow')
for s in range(4):
    austin.forward(300)
    austin.right(90)
austin.end_fill()

# 方法(一):巢狀迴圈
for i in range(6): # 外迴圈重複正方形6次
    for j in range(4): #內迴圈重複4次來畫正方形
        austin.forward(150)
        austin.left(90)
    austin.right(60) #畫下一個正方形前轉彎
# 方法(二):巢狀迴圈 + 加上色彩
colors = ["black","purple","blue","red","pink", "grey"]
for n in range(6):
    austin.color(colors[n])
    for j in range(4): 
        austin.forward(150)
        austin.left(90)
    austin.right(60)

# 方法(三) :巢狀迴圈 + 填滿色彩
colors = ["black","purple","blue","red","pink", "grey"]
for c in range(6):
    austin.color(colors[c])
    austin.begin_fill()
    austin.fillcolor(colors[c])
    for d in range(4):
        austin.forward(150)
        austin.left(90)
    austin.right(60)
austin.end_fill()    
# 方法(二):巢狀迴圈 + 加上色彩
colors = ["black","purple","blue","red","pink", "grey"]
for n in range(6):
    austin.color(colors[n])
    for j in range(4): 
        austin.forward(150)
        austin.left(90)
    austin.right(60)

# 方法(三) :巢狀迴圈 + 填滿色彩
colors = ["black","purple","blue","red","pink", "grey"]
for c in range(6):
    austin.color(colors[c])
    austin.begin_fill()
    austin.fillcolor(colors[c])
    for d in range(4):
        austin.forward(150)
        austin.left(90)
    austin.right(60)
austin.end_fill()