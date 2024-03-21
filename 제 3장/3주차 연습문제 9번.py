Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> result = 0
>>> for i in range(3333, 9999):
	if i % 1234 == 0 :
		continue
	result += i;

	if result + i > 100000:
		break

	
>>> print(result)
97063
>>> 
