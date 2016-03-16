# shapeDrawer.py
# draws user-input shapes in random places on the screen
# with random sizes and colors
 
# bring in the packages of functions we need
import random
import turtle
 
# -------- functions start here ----------------
# make a triangle with random length, color and position with angle of 120
def regular_triangle(myTurtle, x, y, side):
        myTurtle.penup()
        myTurtle.goto(x,y)
        myTurtle.pendown()
        side_count = 0
        myTurtle.color(random.choice(paintball))
        while side_count < 3:
                myTurtle.forward(side)
                myTurtle.right(120)
                side_count = side_count + 1
# make a square with random length, color and position with angle of 90
def regular_square(myTurtle, x, y, side):
        myTurtle.penup()
        myTurtle.goto(x,y)
        myTurtle.pendown()
        side_count = 0
        myTurtle.color(random.choice(paintball))
        while side_count < 4:
                myTurtle.forward(side)
                myTurtle.left(90)
                side_count = side_count + 1
# make a pentagon with random length, color and position with angle of 70
def regular_pentagon(myTurtle, x, y, side):
        myTurtle.penup()
        myTurtle.goto(x,y)
        myTurtle.pendown()
        side_count = 0
        myTurtle.color(random.choice(paintball))
        while side_count < 5:
                myTurtle.forward(side)
                myTurtle.left(70)
                side_count = side_count + 1
 # make a hexagon with random length, color and position with angle of 60
def regular_hexagon(myTurtle, x, y, side):
        myTurtle.penup()
        myTurtle.goto(x,y)
        myTurtle.pendown()
        side_count = 0
        myTurtle.color(random.choice(paintball))
        while side_count < 6:
                myTurtle.forward(side)
                myTurtle.left(60)
                side_count = side_count + 1
# make a octagon with random length, color and position with angle of 45
def regular_octagon(myTurtle, x, y, side):
        myTurtle.penup()
        myTurtle.goto(x,y)
        myTurtle.pendown()
        side_count = 0
        myTurtle.color(random.choice(paintball))
        while side_count < 8:
                myTurtle.forward(side)
                myTurtle.left(45)
                side_count = side_count + 1
# make a circle with a random position and color 
def circle(myTurtle, x, y, radius):
        myTurtle.penup()
        myTurtle.goto(x,y)
        myTurtle.pendown()
        myTurtle.color(random.choice(paintball))
        myTurtle.circle(50)
# make a asterisk with a random positon and color
def asterisk(myTurtle, x, y, side):
        myTurtle.penup()
        myTurtle.goto(x,y)
        myTurtle.pendown()
        side_count = 0
        myTurtle.color(random.choice(paintball))
        while side_count < 3:
                myTurtle.forward(100)
                myTurtle.backward(200)
                myTurtle.forward(100)
                myTurtle.left(60)
                side_count = side_count + 1

# -------- execution starts here ----------------
# prints a welcome statement that tells the user how to use the porgram
print("Welcome to the random shape drawer!")
print("You choose the shapes, and we choose the position, color, and size.")
# creates a turtle
squirt = turtle.Turtle()
# sets a while statement that asks the user for its shape or asks the user if he or she wants to exit  
shape = ""
while shape != "exit":
        print("Enter a shape - your choices are triangle, square, pentagon, hexagon, octagon, circle, and asterisk.")
        print("If you're done making shapes, just type 'exit'.")
        shape = raw_input()
# makes a random side, position and color list and if/elif that decides what the function carrys out depending on what the user puts in
        randx = random.randint(-200,200)
        randy = random.randint(-200,200)
        randside = random.randint(5,100)
        
        paintball = ["green", "blue", "yellow", "red"]
 
        if shape == 'triangle':
                regular_triangle(squirt, randx, randy, randside)
        elif shape == 'square':
                regular_square(squirt, randx, randy, randside)
        elif shape == 'pentagon':
                regular_pentagon(squirt, randx, randy, randside)
        elif shape == 'hexagon:
                regular_hexagon(squirt, randx, randy, randside)
        elif shape == 'octagon':
                regular_octagon(squirt, randx, randy, randside)
        elif shape == 'circle':
                circle(squirt, randx, randy, randside)
        elif shape == 'asterisk':
                asterisk(squirt, randx, randy, randside)

