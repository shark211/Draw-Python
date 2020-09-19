import tkinter
from tkinter import *
#import PIL
#from PIL import Image, ImageTk, ImageDraw

root = Tk()

width = 800
height = 500
c_bg = 'white'
pensize = 5
fg = 'black'

root.geometry("900x650")
root.title('Draw')


c = Canvas(root, width = width, height = height, bg = c_bg)
c.place(x = 0, y = 0)


def paint(event):
    x1,y1=(event.x-1), (event.y-1)
    x2,y2=(event.x+1), (event.y+1)
    c.create_line(x1, y1, x2, y2, width = pensize, fill = fg,capstyle = ROUND, smooth = True)

def changepen1():
	global pensize
	pensize = 5

def changepen2():
	global pensize
	pensize = 10


def changepen3():
	global pensize
	pensize = 30

def changepen4():
	global pensize
	pensize = 50

def changepen5():
	global pensize
	pensize = 100






def redcolor():
    global fg
    fg = 'red'

def bluecolor():
    global fg
    fg = 'blue'


def greencolor():
    global fg
    fg = 'green'

def yellowcolor():
    global fg
    fg = 'yellow'

def whitecolor():
    global fg
    fg = 'white'

def pinkcolor():
    global fg
    fg = 'pink'

def lightbluecolor():
    global fg
    fg = 'lightblue'

def orangecolor():
    global fg
    fg = 'orange'

def blackcolor():
    global fg
    fg = 'black'



def clearc():
  	c.delete(ALL)


def newboi():
	c.delete(ALL)








c.bind('<B1-Motion>', paint)

pensizeb = Button(root, text = "  1 ", font = ("Times", 13, "bold"),relief = GROOVE,command = changepen1 )
pensizeb.place(x = 600, y = 500)

pensize1 = Button(root, text = "  2 ", font = ("Times", 13, "bold"),relief = GROOVE,command = changepen2 )
pensize1.place(x = 650, y = 500)


pensize2 = Button(root, text = "  3 ", font = ("Times", 13, "bold"),relief = GROOVE,command = changepen3 )
pensize2.place(x = 700, y = 500)

pensize3 = Button(root, text = "  4 ", font = ("Times", 13, "bold"),relief = GROOVE,command = changepen4 )
pensize3.place(x = 750, y = 500)


pensize4 = Button(root, text = "  5 ", font = ("Times", 13, "bold"),relief = GROOVE,command = changepen5 )
pensize4.place(x = 800, y = 500)

redb = Button(root, text = "   ", bg = 'red',font = ("Times", 13, "bold"),relief = GROOVE, command = redcolor)
redb.place(x = 10, y = 600)

yellowb = Button(root, text = "   ", bg = 'yellow',font = ("Times", 13, "bold"),relief = GROOVE, command = yellowcolor)
yellowb.place(x = 40, y = 600)

lblueb = Button(root, text = "   ", bg = 'lightblue',font = ("Times", 13, "bold"),relief = GROOVE, command = lightbluecolor)
lblueb.place(x = 70, y = 600)

pinkb = Button(root, text = "   ", bg = 'pink',font = ("Times", 13, "bold"),relief = GROOVE, command = pinkcolor)
pinkb.place(x = 70, y = 560)

blueb = Button(root, text = "   ", bg = 'blue',font = ("Times", 13, "bold"),relief = GROOVE, command = bluecolor)
blueb.place(x = 40, y = 560)

whiteb = Button(root, text = "  ", bg = 'white',font = ("Times", 13, "bold"),relief = GROOVE, command = whitecolor)
whiteb.place(x = 10, y = 560)

blackb = Button(root, text = "   ", bg = 'black',font = ("Times", 13, "bold"),relief = GROOVE, command = blackcolor)
blackb.place(x = 10, y = 520)

greenb = Button(root, text = "   ", bg = 'green',font = ("Times", 13, "bold"),relief = GROOVE, command = greencolor)
greenb.place(x = 40, y = 520)

orangeb = Button(root, text = "   ", bg = 'orange',font = ("Times", 13, "bold"),relief = GROOVE, command = orangecolor)
orangeb.place(x = 70, y = 520)

pb = Button(root, text = "  P ", font = ("Times", 13, "bold"),relief = GROOVE,command = blackcolor )
pb.place(x = 650, y = 550)

eb = Button(root, text = "  E ", font = ("Times", 13, "bold"),relief = GROOVE,command = whitecolor)
eb.place(x = 700, y = 550)

cb = Button(root, text = "  C ", font = ("Times", 13, "bold"),relief = GROOVE,command = clearc)
cb.place(x = 750, y = 550)

newb = Button(root, text = "New", font = ("Times", 15, "bold"), command = newboi)
newb.place(x = 350, y = 550)



root.mainloop()
