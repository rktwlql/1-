Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def plus(v1, v2, v3) :
	result = 0
	result = v1 + v2 + v3
	return result
hap = plus(100, 200, 300)
SyntaxError: invalid syntax
>>> def plus(v1, v2, v3) :
	result = 0
	result = v1 + v2 + v3
	return result
hap = 0
SyntaxError: invalid syntax
>>> def plus(v1, v2, v3) :
	result = 0
	result = v1 + v2 + v3
	return result

>>> hap = 0
>>> hap = plus(100, 200, 300)
>>> print(hap)
600
>>> 
>>> def f1():
	print(var)

	
>>> def f2():
	var = 10
	print(var)

	
>>> var = 100
>>> f1()
100
>>> f2()
10
>>> 
>>> 
>>> def addnumber(num):
	if(num < 2): return 1
	else : return num + addnumber(num-1)

	
>>> print(addnumber(100))
5050
>>> 
>>> 
>>> def myFunc(p1, p2, p3):
	ret = p1 + p2 + p3
	return ret

>>> print("매개변수 없이 호출 ==> ", myFunc())
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    print("매개변수 없이 호출 ==> ", myFunc())
TypeError: myFunc() missing 3 required positional arguments: 'p1', 'p2', and 'p3'
>>> def myFunc(p1, p2 = 'p2', p3 = 'p3'):
	ret = p1 + p2 + p3
	return ret

>>> print("매개변수 없이 호출 ==> ", myFunc())
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    print("매개변수 없이 호출 ==> ", myFunc())
TypeError: myFunc() missing 1 required positional argument: 'p1'
>>> def myFunc(p1, p2 'p2', p3='p3'):
	ret = p1 + p2 + p3
	return ret
SyntaxError: invalid syntax
>>> def myFunc(p1, p2='p2', p3='p3'):
	ret = p1 + p2 + p3
	return ret

>>> 
KeyboardInterrupt
>>> print("매개변수 없이 호출 ==> ", myFunc())
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    print("매개변수 없이 호출 ==> ", myFunc())
TypeError: myFunc() missing 1 required positional argument: 'p1'
>>> print("매개변수 없이 호출 ==> ", myFunc())
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    print("매개변수 없이 호출 ==> ", myFunc())
TypeError: myFunc() missing 1 required positional argument: 'p1'
>>> 
