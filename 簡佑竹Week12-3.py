Python 3.7.7 (bundled)
>>> # [1,2,3,4,5]
a = [0,1,2,3,4] 
print(a)
[0, 1, 2, 3, 4]

a = range(0,5,1) #初值預設為0 差距預設為1
print(a)
range(0, 5)

a = range(0,5)
print(a)
range(0, 5)

a = range(5)
print(a)
range(0, 5)

print(a[0], a[1], a[2], a[3], a[4]) #index
0 1 2 3 4

# [2,3,4,5]
b = range(2,6) #range(2,6,1)
print(b[0], b[1], b[2], b[3])
2 3 4 5

# [2,5,8]
c = range(2,10,3) #終值到10前一個數字9
print(c[0], c[1], c[2])
2 5 8

# [10,8,6,4]
d = range(10,3,-2)
print(d[0], d[1], d[2], d[3])
10 8 6 4

隨堂練習
a = range(10)
print(a[0], a[1], a[2], a[3], a[4], a[5], a[6], a[7], a[8], a[9])
0 1 2 3 4 5 6 7 8 9

b = range(0,9,2)
print(b[0], b[1], b[2], b[3], b[4])
0 2 4 6 8

c = range(5,10,2)
print(c[0], c[1], c[2])
5 7 9

d = range(0,-10,-1)
print(d[0], d[1], d[2], d[3], d[4], d[5], d[6], d[7], d[8], d[9])
0 -1 -2 -3 -4 -5 -6 -7 -8 -9