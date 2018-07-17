#
import tkinter
from tkinter import *
import math
#
tk=Tk()
tk.title("Sample")
#
canvas=Canvas(tk)
canvas["height"]=600
canvas["width"]=800
canvas["background"]="#ddddff"
canvas["borderwidth"]=2
canvas.pack()
#

#
canvas.create_text(20,20,text="20,10")
canvas.create_text(780,550,text="780,550")
#
points=[]
points2=[]
ay=290
y0=290
x0=50
x1=790
dx=10
#
for n in range (x0,x1,dx):
    y=y0-ay*math.cos(n*dx)
    pp=(n,y)
    points.append(pp)
#
canvas.create_line(points,fill="blue",smooth=1)
#
for n in range (x0,x1,dx):
    y2=y0-ay*1.2*(math.cos(n*dx))
    pp2=(n,y2)
    points2.append(pp2)
#
canvas.create_line(points2,fill="red",smooth=1)
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