Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from tkinter import *
>>> window = TK()
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    window = TK()
NameError: name 'TK' is not defined
>>> window = Tk()
>>> 
>>> button1 = Button(window, text = "버튼1")
>>> button2 = Button(window, text = "버튼2")
>>> button3 = Button(window, text = "버튼3")
>>> 
>>> button1.pack(side = LEFT)
>>> button2.pack(side = LEFT)
>>> button3.pack(side = LEFT)
>>> "빈 칸에는 LEFT 가 들어가야 한다"
'빈 칸에는 LEFT 가 들어가야 한다'
>>> window.mainloop()
"2번 보기를 만들기 위해서는 RIGHT를 입력하면 된다"
"3번 보기를 만들기 위해서는 TOP를 입력하면 된다"
"4번 보기를 만들기 위해서는 BOTTOM을 입력하면 된다"
