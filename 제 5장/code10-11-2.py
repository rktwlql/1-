Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import tkinter
>>> import random
>>> 
>>> from tkinter import *
>>> from random import shuffle
>>> 
>>> btnList = [None]*9
>>> fnameList = ["honeycomb.gif", "icecream.gif", "jellybean.gif", "kitkat.gif", "lollipop.gif", "marshmallow.gif", "nougat.gif", "oreo.gif", "pie.gif"]
>>> photoList = [None]*9
>>> i, k = 0, 0
>>> xPos, yPos = 0, 0
>>> num = 0
>>> 
>>> shuffle(fnameList)
>>> 
>>> window = Tk()
>>> window.geometry("210x210")
''
>>> for i in range(0, 9):
	photoList[i] = PhotoImage(file = "jpg/" + fnameList[i])
	btnList[i] = Button(window, image = photoList[i])

	
Traceback (most recent call last):
  File "<pyshell#18>", line 2, in <module>
    photoList[i] = PhotoImage(file = "jpg/" + fnameList[i])
  File "C:\Users\marine\AppData\Local\Programs\Python\Python37\lib\tkinter\__init__.py", line 3545, in __init__
    Image.__init__(self, 'photo', name, cnf, master, **kw)
  File "C:\Users\marine\AppData\Local\Programs\Python\Python37\lib\tkinter\__init__.py", line 3501, in __init__
    self.tk.call(('image', 'create', imgtype, name,) + options)
_tkinter.TclError: couldn't open "jpg/lollipop.gif": no such file or directory
>>> for i in range(0, 3):
	for k in range(0, 3) :
		btnList[num].place(x = xPos, y = yPos)
		num += 1
		xPos += 70
	xPos = 0
	yPos += 70

	
Traceback (most recent call last):
  File "<pyshell#26>", line 3, in <module>
    btnList[num].place(x = xPos, y = yPos)
AttributeError: 'NoneType' object has no attribute 'place'
>>> window.mainloop()
