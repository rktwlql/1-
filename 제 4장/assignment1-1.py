Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> ss = 'Python'
>>> for i in range(0,len(ss)):
	print(ss[i] + '$', end = ")
	      
SyntaxError: EOL while scanning string literal
>>> ss = 'Python'
	      
>>> for i in range(0,len(ss)):
	print(ss[i] + '$', end = ' ')

	      
P$ y$ t$ h$ o$ n$ 
>>> inStr=input("문자를 입력 :")
	      
문자를 입력 : 파이썬 ### CookBook $$$ @@@ 열공중 1234
>>> outstr = ""
	      
>>> import = re
	      
SyntaxError: invalid syntax
>>> import re
	      
>>> re.sub('[^A-Za-z0-9가-힣]', '', inStr)
	      
'파이썬CookBook열공중1234'
>>> 
	      
>>>  inStr, outStr = "Python", ""
	      
SyntaxError: unexpected indent
>>> inStr, outStr = "Python", ""
	      
\
>>> inStr, outStr = "Python", ""
	      
>>> strLen = len(inStr)
	      
>>> for i in range(0, strLen):
	      outStr += inStr[strLen-(i+1)]

	      
>>> print("내용을 거꾸로 출력 --> %s" % outStr)
	      
내용을 거꾸로 출력 --> nohtyP
>>> 
