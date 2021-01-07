# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# 奇偶數判斷
number = int(input('Given a number: '))
condition = number%2
if condition == 0:
    print('This number is an even number.')
else:
    print('This number is an odd number.')
    
# 閏年判斷
year = int(input('Given a year: '))
if year%400 == 0:
    print(year,'是閏年')
elif year%100 == 0:
    print(year,'不是閏年')
elif year%4 == 0:
    print(year,'是閏年')
else:
    print(year,'不是閏年')
    
# 分數與評語
score = int(input('Given a score: '))
if score >= 80:
    print('非常好!')
elif score >= 60:
    print('不錯喔~')
else:
    print('要加油!')    

#條件迴圈    
n = 1
while n < 10:
    print('變數n是', n)
    n = n + 1
print('Finished')