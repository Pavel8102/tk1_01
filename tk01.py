#
import tkinter
from tkinter import *
import math
#
tk=Tk()
tk.title("Sample")
#
canvas=Canvas(tk)
canvas["height"]=360
canvas["width"]=480
canvas["background"]="#ddddff"
canvas["borderwidth"]=2
canvas.pack()
#

#
canvas.create_text(20,20,text="20,10")
canvas.create_text(460,350,text="460,350")
#
points=[]
ay=150
y0=150
x0=50
x1=470
dx=10
#
for n in range (x0,x1,dx):
    y=y0-ay*math.cos(n*dx)
    pp=(n,y)
    points.append(pp)
#
canvas.create_line(points,fill="blue",smooth=1)
#
y_axe =[]
yy=(x0,0)
y_axe.append(yy)
yy=(x0,y0+ay)
y_axe.append(yy)
canvas.create_line(y_axe,fill="black",width=2)
#
x_axe=[]
xx=(x0,y0)
x_axe.append(xx)
xx=(x1,y0)
x_axe.append(xx)
canvas.create_line(x_axe,fill ="black",width=2)
#
tk.mainloop()