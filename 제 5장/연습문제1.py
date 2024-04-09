Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from tkinter import *
>>> window = Tk()
>>> 
>>> def rdo_change():
	if var.get() ==1:
		label1.configure(text = "벤츠")
	else :
		label1.configure(text = "포르쉐")

		
>>> var = IntVar()
>>> rdo1 = Radiobutton(window, text = "벤츠", variable = var, value = 1, command = rdo_change)
>>> rdo2 = Radiobutton(window, text = "포르쉐", variable = var, value = 2, command = rdo_change)
>>> label1 = Label(window, text = "선택한 차량", fg="red")
>>> 
>>> rdo1.pack()
>>> rdo2.pack()
>>> label.pack()
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    label.pack()
NameError: name 'label' is not defined
>>> 
>>> label1.pack()
>>> window.mainloop()
