import tkinter
import oop
myP = oop.Point(1, 2)
"""print(myP._color)""" #you can still access the private variable, but you shouldn't do it this way. Instead, do it this way:
print(myP.getColor())

"""print(myP.__name)"""  #will give error, because it is private - no attribute error. There is a trick to get around this, but programmers trust ppl to never use the trick.
import dunder
exec("dunder")#executes a program in the 
"""eval('print("hi"))"""  #this would evaluate the following string as if it was a python command - but better for single line commands.

w=tkinter.StringVar()
w.trace()