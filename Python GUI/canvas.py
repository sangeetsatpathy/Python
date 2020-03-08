from tkinter import *
#NOTE: when using canvas, the shapes that are defined later will always go above the earlier shapes, so it overlaps.
#in canvas, all the shapes are called using the same starting: "Canvas obj.create_" and then the suffix is the shape you want to draw, like create_polygon() and create_arc()
window = Tk()
#A canvas is a component where images and shapes are coded and drawn, either from the programmer or the user.
c = Canvas(window, width=300, height=200)#as always, 1st arg = container, width and height in pixels, from (0,0) being at the top-left corner.
c.pack()
c.create_line(0,0,300,200, fill="Blue", width=5)#creates a line - in Canvas, most of the shapes are created with the "create_" and a suffix of the object you want to draw.
#Line: 1st arg = x1; 2nd arg = y1; 3rd arg = x2, 4th arg = y2(top-left = (0,0)) fill is the color for the line to be. Width is the boldness or thickness
c.create_rectangle(100,100,300,200, fill="Red")#rectangle needs 2 points, which are diagonal: like line: 1-x1; 2-y1; 3-x2; 4-y2   fill is the color to fill the rect with.
c.create_oval(200,50,250,60, fill="Green")#creates an oval out of a rectangle - the points given are the same as the rectangle, and the oval intersects the top middle, bottom middle, and both of the sides' middles.
window.mainloop()