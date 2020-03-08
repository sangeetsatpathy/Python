from tkinter import *
#If you are already using grid, tthen you cannot use pack after.
window = Tk()

labelUser = Label(window, text="Username:")
labelPass = Label(window, text="Psw:")
eUser = Entry(window)
ePass = Entry(window)
#grid() is like a layout manager, which also makes components visible at the same time. It's a table, with rows and columns
labelUser.grid(row=0, sticky=E)#specifies the row(first row = 0, left to right), sticky tells it to align the label (N,S,E,W - North(up),etc.)
labelPass.grid(row=1, sticky=E)
eUser.grid(row=0, column=1)#both row and column, column starts at 0 from top, default value is 0.
ePass.grid(row=1, column=1)
window.mainloop()