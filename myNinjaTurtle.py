# myNinjaTurtle.py

import turtle

def makeHexagon(myTurtle, side):
	myTurtle.forward(side)
	myTurtle.left(60)
	myTurtle.forward(side)
        myTurtle.left(60)
	myTurtle.forward(side)
        myTurtle.left(60)
	myTurtle.forward(side)
        myTurtle.left(60)
	myTurtle.forward(side)
        myTurtle.left(60)
	myTurtle.forward(side)
        myTurtle.left(60)

# make our turtle
squirt = turtle.Turtle()
squirt.forward(100)
squirt.left(60)
squirt.forward(100)
squirt.left(60)
squirt.forward(100)
squirt.left(60)

length = 100
while length > 0:
	makeHexagon(squirt, length)
# rotate and make the sides shorter
	squirt.right(5)

length = 100
while length > 0:
	makeHexagon(squirt, length)
# rotate and make the sides shorter
	squirt.right(5)
	length = length - 1

turtle.exitonclick()

	

