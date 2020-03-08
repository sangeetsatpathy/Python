import tkinter
"""
from tkinter import * - from tkinter, import everything, so you don't have to write tkinter each time"""

window = tkinter.Tk()#the Tk() class represents the windows in python gui - it is in the tkinter library

lbl = tkinter.Label(window,text="Hello World")#1st arg = the container of label, rest = the features : including the text; this is a label component
lbl.pack()#makes it visible - optional arg = position

fTop = tkinter.Frame(window)#frames are components that hold smaller components (like JPanel)
fTop.pack(side=tkinter.TOP)#makes it visible, specifying the top side.

fBot = tkinter.Frame(window)#1st arg = the container for it(like all components)
fBot.pack(side=tkinter.BOTTOM)

lbl2 = tkinter.Label(fBot,text="testing")#this label is inside the frame,acts as container
lbl2.pack(side=tkinter.LEFT)#to the left of bottom panel

def onClick():#doesn't take in self because it is a command - no object instance
	print("Button Clicked.")

btn=tkinter.Button(fBot, bd=5,bg="Green",fg = "White", text="Click Here for More!",padx=50, pady=25, command=onClick)#creates a button - its border length(outer wall width on both sides) is 15 pixels - default is 2. 
	#The background color(bg) is a string - in this case-green.
	#The foreground (text) color is white. 
	#padx and pady are the padding(from text/middle) for the x and y direction, both numbers.
	#the command tells us which function will be called every time button is clicked.
btn.pack(side=tkinter.RIGHT)#to the right of bottom panel.
"""could also do: 
btn.place(x=50,y=50)-defines the x and y coordinates of the middle of the button."""

scale = tkinter.scale(window,from_=0, to_=50,orient=HORIZONTAL)#A scale/slider w/ #s 
#the from_ and to_ attributes are the min and max values of the scale
#orient attribute is optional, VERTICAL or HORIZONTAL - the way to orient itself
scale.pack()

window.mainloop()#keeps looping the window until it closes - always at very end of the code