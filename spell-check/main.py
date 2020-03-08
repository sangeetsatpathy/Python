from tkinter import *

master=Tk()


fTop = Frame(master)
fTop.pack(side=TOP)

fBot = Frame(master)
fBot.pack(side=BOTTOM)

lbl= Label(fTop, text="Try to find as many 3-letter words as possible")
lbl.pack()

i=0
txt=""
lst = ["cad","cab","dab","bad"]

def onClicka():
	global i
	global txt
	global lst
	i+=1
	if(i<3):
		print("a", end="")
		txt=txt+"a"
	elif(i==3):
		print("a", end="")
		txt=txt+"a"
		print("\nChecking...\n", end="")
		if(txt==lst[0] or txt==lst[1] or txt==lst[2] or txt==lst[3]):
			print(txt+" is correct! Try another one!")
			txt=""
		else:
			print(txt+" isn't a word - better luck next time!")
			txt=""
		i=0
def onClickb():
	global i
	global txt
	global lst
	i+=1
	if(i<3):
		print("b", end="")
		txt=txt+"b"
	elif(i==3):
		print("b", end="")
		txt=txt+"b"
		print("\nChecking...\n", end="")
		if(txt==lst[0] or txt==lst[1] or txt==lst[2] or txt==lst[3]):
			print(txt+" is correct! Try another one!")
			txt=""
		else:
			print(txt+" isn't a word - better luck next time!")
			txt=""
		i=0
def onClickc():
	global i
	global txt
	global lst
	i+=1
	if(i<3):
		print("c", end="")
		txt=txt+"c"
	elif(i==3):
		print("c", end="")
		txt=txt+"c"
		print("\nChecking...\n", end="")
		if(txt==lst[0] or txt==lst[1] or txt==lst[2] or txt==lst[3]):
			print(txt+" is correct! Try another one!")
			txt=""
		else:
			print(txt+" isn't a word - better luck next time!")
			txt=""
		i=0

def onClickd():
	global i
	global txt
	global lst
	i+=1
	if(i<3):
		print("d", end="")
		txt=txt+"d"
	elif(i==3):
		print("d", end="")
		txt=txt+"d"
		print("\nChecking...\n", end="")
		if(txt==lst[0] or txt==lst[1] or txt==lst[2] or txt==lst[3]):
			print(txt+" is correct! Try another one!")
			txt=""
		else:
			print(txt+" isn't a word - better luck next time!")
			txt=""
		i=0

btn = Button(fBot,text="a",padx=50, pady=25, command =onClicka)
btn.pack(side=LEFT)

btnNumber1 = Button(fBot,text="b",padx=50, pady=25, command = onClickb)
btnNumber1.pack(side=RIGHT)

btnNumber2 = Button(fBot,text="c",padx=50, pady=25, command = onClickc)
btnNumber2.pack(side=TOP)

btnNumber3 = Button(fBot,text="d",padx=50, pady=25, command = onClickd)
btnNumber3.pack(side=BOTTOM)

master.mainloop()