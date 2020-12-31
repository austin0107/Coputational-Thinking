True
True

False
False

print(False+ 5)
5

print(True+ 5)
6

bool(0)
False

bool(1)
True

bool(2)
True

bool(-5)
True

bool()
False

name="Zoe"
name=="zoe"
False

name="Zoe"
name!="zoe"
True

name="Zoe"
name>="zoe"
False

print(9==7)
False
print(9<=7)
False
print(9>=7)
True
print(9>7)
True
print(9<7)
False
print(9!=7)
True

movie_rating=8.8
print(type(movie_rating>=8.0))
<class 'bool'>
print(movie_rating>=8.0)
True

x=70
(x>60) and (x<80)
True

x=80
(x>100) or (x<100)
True

x=100
not(x!=120)
False

print("H" in "Hello world")
True
print("h" in "Hello world")
False

print(9 is 9)
True
print(9 is not 9)
False
print(9 is 9.0)
False
print(9 is not 9.0)
True
print(9 is not "9")
True

sunny = False
if sunny:
   print("Go outside")
    
sunny = True
if sunny:
   print("Go outside")
Go outside

num = int(input("enter a number: "))
if num > 3:
   print(num,"> 3")
print("end")
enter a number: 10
10 > 3
end

 score = int(input('enter a number '))
if score >= 70:
    print('good')
else :
    print('try again')
enter a number 70
good