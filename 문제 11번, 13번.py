Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> '문제 11번'
'문제 11번'
>>> print(int('1011',2))
11
>>> print(int('1A',16))
26
>>> 
>>> '문제 13
SyntaxError: EOL while scanning string literal
>>> '문제 13번'
'문제 13번'
>>> 
>>> int('1002',2)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    int('1002',2)
ValueError: invalid literal for int() with base 2: '1002'
>>> print(int('1002',2))
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    print(int('1002',2))
ValueError: invalid literal for int() with base 2: '1002'
>>> int('1008',8)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    int('1008',8)
ValueError: invalid literal for int() with base 8: '1008'
>>> int('AAFG',16)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    int('AAFG',16)
ValueError: invalid literal for int() with base 16: 'AAFG'
>>> "모든 변환될 수가 해당 진법을 따르지 않음'
SyntaxError: EOL while scanning string literal
>>> "모든 변환될 수가 해당 진법을 따르지 않음"
'모든 변환될 수가 해당 진법을 따르지 않음'
>>> 
