Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> import math
>>> import random
>>> swidth, sheight = 500, 500
>>> txtSize = 20
>>> 
>>> turtle.title('거북이 나선 문자열')
>>> turtle.setup(width =  swidth, height = sheight)
>>> turtle.screensize(swidth, sheight)
>>> turtle.penup()
>>> 
>>> string = turtle.textinput('문자열 입력', '거북이가 쓸 문자열을 입력')
>>> 
>>> length = len(string)
>>> angle = 0
>>> rotate = 360*2/length
>>> rotate_dec = swidth/2/length
>>> turtle = turtle.Turtle()
>>> turtle.shape('turtle')
>>> turtle.penup()
>>> 
>>> for character in string:
	radian = 3.14 * angle / 180
	tX = radius * math.cos(radian)
	tY = radius * math.sin(radian)
	turtle.goto(tX, tY)
	r=random.random(); g=random.random(); b=random.random()
	turtle.pencolor((r,g,b))
	turtle.write(character, font=('맑은 고딕', txtSize, 'bold'))
	angle += rotate
	radius -= rotate_dec
	turtle.hideturtle()

	
Traceback (most recent call last):
  File "<pyshell#32>", line 3, in <module>
    tX = radius * math.cos(radian)
NameError: name 'radius' is not defined
>>> radius=200
>>> for character in string:
	radian = 3.14 * angle / 180
	tX = radius * math.cos(radian)
	tY = radius * math.sin(radian)
	turtle.goto(tX, tY)
	r=random.random(); g=random.random(); b=random.random()
	turtle.pencolor((r,g,b))
	turtle.write(character, font=('맑은 고딕', txtSize, 'bold'))
	angle += rotate
	radius -= rotate_dec
	turtle.hideturtle()

	
>>> 
