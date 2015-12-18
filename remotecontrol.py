import turtle
from Tkinter import *

# create the root Tkinter window and a Frame to go in it
root = Tk()
frame = Frame(root)

# create our turtle
shawn = turtle.Turtle()

# create a design
myTurtle = turtle.Turtle()
def pentagon(myTurtle, size):
	five = 0
	myTurtle.color('green')
	while five < 5:
		myTurtle.forward(100)
		myTurtle.left(70)
		five = five + 1
shape = Button(frame, text='shape', command=lambda: regular_pentagon())
# make some simple buttons
fwd = Button(frame, text='fwd', command=lambda: shawn.forward(50))
bwd = Button(frame, text='bwd', command=lambda: shawn.backward(50))
left = Button(frame, text='left', command=lambda: shawn.left(90))
right = Button(frame, text='right', command=lambda: shawn.right(90))
penup = Button(frame, text='penup', command=lambda: shawn.penup())
pendown = Button(frame, text='pendown', command=lambda: shawn.pendown())
green = Button(frame, text='green', command=lambda: shawn.color('green'))
red = Button(frame, text='red', command=lambda: shawn.color('red'))
blue = Button(frame, text='blue', command=lambda: shawn.color('blue'))
black = Button(frame, text='black', command=lambda: shawn.color('black'))

# put it all together
fwd.pack(side=LEFT)
bwd.pack(side=LEFT)
left.pack(side=LEFT)
right.pack(side=LEFT)
penup.pack(side=LEFT)
pendown.pack(side=LEFT)
green.pack(side=LEFT)
red.pack(side=LEFT)
blue.pack(side=LEFT)
black.pack(side=LEFT)
shape.pack(side=LEFT)
frame.pack()

turtle.exitonclick()
