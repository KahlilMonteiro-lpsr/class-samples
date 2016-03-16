import turtle

def  drawTee(myTurtle):
	count = 0
	while count < 4:
		drawFourTees(myTurtle)
		count = count + 1

def drawFourTees(myTurtle):
	myTurtle.forward(200)
	myTurtle.backward(50)
	myTurtle.right(90)
	myTurtle.forward(50)
	myTurtle.backward(100)
	myTurtle.forward(50)
	myTurtle.right(90)
	myTurtle.forward(150)
	myTurtle.right(90)

# make your turtle down here and pass it to the appropriate places

noah = turtle.Turtle()
count = 0
while count < 4:
	drawTee(noah)
	count = count + 1

turtle.exitonclick()
