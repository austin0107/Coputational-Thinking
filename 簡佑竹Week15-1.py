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