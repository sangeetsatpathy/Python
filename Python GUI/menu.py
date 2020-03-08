from tkinter import *

window = Tk()

mainMenu = Menu(window)#A menu is like when you see 'File' or 'Edit on the top of an application
window.config(menu=mainMenu)#configures the window, and the menu command changes the default menu to the specified one

def test():
    print("hhhh")

fileMenu = Menu(mainMenu)#the menu is inside the mainMenu - it is the menu containing all the components of the cascade
mainMenu.add_cascade(label="File", menu=fileMenu)#add_cascade method adds a dropdown menu like for example when you click File. label = the text displayed; 2nd arg is the menu where the cascade and its constituents are stored in
fileMenu.add_command(label="Open", command=test)#adds each command/component to the fileMenu(the menu containing these.) - there is a label, and command arg decides which function to call when this is clicked.
fileMenu.add_command(label="Save", command=test)
fileMenu.add_separator()#adds a separator(a line separating commands to group them) instead of a command
fileMenu.add_command(label="Close", command=test)

editMenu = Menu(mainMenu)
mainMenu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Undo")
editMenu.add_command(label="Redo")

mainMenu.add_command(label="Help")#when you call the add_command directly to the mainMenu(or the supreme menu containing the cascades and subMenus), it is not a cascade and it is instead like a button in the menu.

window.mainloop()