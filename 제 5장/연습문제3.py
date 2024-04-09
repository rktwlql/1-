Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from tkinter import *
>>> from time import *
>>> 
>>> fnameList = ["jeju1.gif", "jeju2.gif", "jeju3.gif", "jeju4.gif", "jeju5.gif", "jeju6.gif", "jeju7.gif", "jeju8.gif","jeju9.gif"]
>>> num = 0
>>> 
>>> def clickNext():
	global num
	num+= 1
	if num > 8:
		num = 0
	photo = PhotoImage(file = "gif/" +fnameList[num])
	pLabel.image = photo

	
>>> def clickPrev():
	global num
	num-= 1
	if num < 0:
		num = 8
	photo = PhotoImage(file = "gif/" +fnameList[num])
	pLabel.image = photo

>>> 
