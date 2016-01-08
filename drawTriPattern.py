import turtle

def drawTriangle(myTurtle):
	myTurtle.penup()
	myTurtle.forward(10)
	myTurtle.pendown()
	myTurtle.left(120)
	myTurtle.forward(10)
        myTurtle.left(120)
	myTurtle.forward(10)
        myTurtle.left(120)
	myTurtle.forward(10)

def drawRowofTriangles(myTurtle):
	count = 0
	while count < 4:
		myTurtle.pendown()
		drawTriangle(myTurtle)
		myTurtle.penup()
		myTurtle.forward(10)
		count = count + 1

def drawThreeRowsofTriangles(myTurtle):
	count = 0
	while count < 3:
		myTurtle.goto(0,0)
		myTurtle.left(30)
		drawRowofTriangles(myTurtle)
		count = count + 1

noah = turtle.Turtle()
drawThreeRowsofTriangles(noah)
noah.left(120)
drawThreeRowsofTriangles(noah)

turtle.exitonclick()



