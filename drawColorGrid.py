import turtle

def drawSquare(myTurtle):
	myTurtle.forward(20)
	myTurtle.right(90)
	myTurtle.forward(20)
	myTurtle.right(90)
        myTurtle.forward(20)
        myTurtle.right(90)
	myTurtle.forward(20)
	myTurtle.backward(10)
	myTurtle.right(90)
	myTurtle.forward(20)
	myTurtle.backward(10)
	myTurtle.left(90)
	myTurtle.forward(10)
	myTurtle.backward(20)

def drawColorSquare(myTurtle):
	count = 0
	while count < 1:
		myTurtle.right(90)
		drawSquare(myTurtle)
		count = count + 1

def drawRowofSquares(myTurtle):
	count = 0
	while count < 3:
		myTurtle.right(90)
		drawColorSquare(myTurtle)
		count=count + 1

noah = turtle.Turtle()
drawRowofSquares(noah)
noah.right(90)
drawRowofSquares(noah)

turtle.exitonclick()
