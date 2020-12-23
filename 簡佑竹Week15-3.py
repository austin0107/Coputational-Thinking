# 畫出幾何圖案(一):六角型
import turtle
a=turtle.Turtle()
for i in range(6): # 重複6次:前進並轉彎
    a.forward(250) 
    a.left(60)
# 畫出幾何圖案(二):重複六角型
import turtle
a=turtle.Turtle()
for i in range(36): # 重複6次:前進並轉彎
    for j in range(6):
        a.forward(250)
        a.left(60)
    a.right(10) #加入轉彎
# 畫出幾何圖案(三):彩虹重複六角型
import turtle
a=turtle.Turtle()
turtle.bgcolor("black") # 把背景變黑
colors = ["red","orange","yellow","green","blue","purple"]
for i in range(36):
    for j in range(6):
        a.color(colors[j]) #選擇j位置的顏色
        a.forward(250)
        a.left(60)
    a.right(10)
# 畫出幾何圖案(四):小圓圈彩虹重複六角型
a.penup() # 畫36個小圓圈
a.color("white")
for i in range(36): # 重複36次,找到對應的六角形
    a.forward(500)
    a.pendown()
    a.circle(5)
    a.penup()
    a.backward(500)
    a.right(10) # 隱藏海龜
a.hideturtle()
