#the variable classes are IntVar, StringVar, DoubleVar, and BooleanVar, all of which have the trace() method to attach "observer" callbacks - see entry.py for more info on the trace method
from tkinter import *
master = Tk() 
def callback(*args):# say "*args" if the arguments are ignored
	print("Variable Changed! WOW!")
	print("Chocolate Topping: {}".format(bool(var1.get())))
var1 = IntVar()
var1.trace("w",callback)#the callback function doesn't have to be a lambda


checkbox1 = Checkbutton(master, text='Chocolate', variable=var1).grid(row=0, sticky=W)
#Checkbutton parameter 1 is the container, text is the text to be displayed next to the check box, and the variable parameter is the variable where all the info is stored in - connects the checkbutton to the IntVar


def printValue():
	print("Variable Changed! WOW!")
	print("Vanilla Topping: {}".format(bool(var2.get())))
var2 = IntVar()#IntVar is a Variable Class, like StringVar and is used to represent the values of checkboxes/checkbuttons.
var2.trace("w",lambda *args:printValue())
checkbox2 = Checkbutton(master, text='Vanilla', variable=var2).grid(row=1, sticky=W) 


def outValue():
	print(radio.get())#just radio.get will return the value we assigned to each of the radiobuttons - the number that identifies it.
radio = IntVar()#Intvar is used for radiobuttons, too.
radio.trace("w", lambda *args: outValue())
rad_but_1 = Radiobutton(master, text='Coffee', variable=radio, value=1).grid(sticky=W)#text is the text to be displayed next to the radiobutton, the value param is an int because we are using IntVar - without it, the Radiobuttons wouldn't be separate - each radiobutton needs a diff. value. The variable param connects the Radiobutton w/ IntVar.
rad_but_2 = Radiobutton(master, text='Tea', variable=radio, value=2).grid(sticky=W)

mainloop() 