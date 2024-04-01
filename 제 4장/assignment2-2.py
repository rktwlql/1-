Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def myFunc(p1, p2=p2, p3=p3):
	ret = p1 + p2 + p3
	return ret

Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    def myFunc(p1, p2=p2, p3=p3):
NameError: name 'p2' is not defined
>>> def myFunc(p1 ='p1', p2 = 'p2', p3 = 'p3'):
	ret = p1 + p2 + p3
	return ret

>>> print("매개변수 없이 호출 ==> ", myFunc())
매개변수 없이 호출 ==>  p1p2p3
>>> def myFunc(p1 = 1, p2 = 2, p3 = 3):
	ret = p1 + p2 + p3
	return ret

>>> print("매개변수 없이 호출 ==> ", myFunc())
매개변수 없이 호출 ==>  6
>>> print("매개변수가 1개로 호출 ==> ", myFunc(1))
매개변수가 1개로 호출 ==>  6
>>> print("매개변수가 2개로 호출 ==> ", myFunc(1,2))
매개변수가 2개로 호출 ==>  6
>>> print("매개변수가 3개로 호출 ==> ", myFunc(1,2,3))
매개변수가 3개로 호출 ==>  6
>>> 
