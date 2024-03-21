Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> nn = [ 100, 200, 300, 400, 500 ]
>>> nn[1] = 777
>>> print(nn)
[100, 777, 300, 400, 500]
>>> nn[1] = [444, 555]
>>> print(nn)
[100, [444, 555], 300, 400, 500]
>>> nn = [100, 200, 300, 400, 500]
>>> nn[1:4] = [444,555]
>>> print(nn)
[100, 444, 555, 500]
>>> nn = [100, 200, 300, 400, 500]
>>> nn[2:] = []
>>> print(nn)
[100, 200]
>>> 
