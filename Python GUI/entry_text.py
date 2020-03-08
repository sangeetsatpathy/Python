from tkinter import*
#every time a character is changed, it will print what is there.
master = Tk()

def PrintValue():
	print(whatUserWrote.get())#prints the value of the StringVar object; the get method is in all the variable classes - BooleanVar, StringVar, IntVar, and DoubleVar
whatUserWrote = StringVar()#StringVar() class designed to take in user input in the form of text
whatUserWrote.trace("w", lambda name, index, mode: PrintValue())#returns the callback function (which in this case calls the PrintValue() function.)
	#first parameter is the mode - "w" is for write, "r" for read, and "u" for undefined
	# 2nd arg is the callback function(the function called when the variable is written, read, or undefined) - passed w/ 3 vars: name, index, and mode, and we call the PrintValue function that we define (and of course the self).
		#name is the internal variable name- in this case, whatUserWrote(the StringVar)
		#variable index - if the internal variable is a list, then it is an index into that list. If a scalar(single) variable, it is the empty string
		#the operation/mode - r, w, or u (which we wrote earlier)
"""To ignore the args, replace them with: *args"""
en = Entry(master,fg="White", bg="Black", bd=5, textvariable=whatUserWrote, width=20)#an entry is a text input
	#fg is the text input you give (foreground)-white
	#bg the background color is black
	#the border length is 15 - the border (outer wall) width
	#textvariable is the variable that all the text inputted is stored inside of(for strings), similar to variable for other components(like RadioList and CheckButtons)
	#width is the width in # of characters
en.pack()


s=Scrollbar(master)
s.pack(side=RIGHT, fill=Y)#1 = what side it is(so it doesn't overlap with the text box). 2=the direction it can spread across-can be BOTH(optional)



#the text object takes in multiple lines of text input. There is no function on its own that lets us take in user input - we can use a button with it.
T = Text(master, height=2, width=30, yscrollcommand = s.set)#height is in lines, length is in the # of characters.
#yscrollcommand is telling us that we set a scrollbar to be the y-axis scrollbar (there is an xscrollcommand, too)
T.pack() 
T.insert(END, 'GeeksforGeeks\nBEST WEBSITE\n')#the END argument means that insert the code at the end of the previous text(if there is any)
s.config(command = T.xview)#allows us to click the up and down arrows to go up and down(if we say xview, it will do the side to side arrow - has to match the direction of the scrollbar)
master.mainloop()