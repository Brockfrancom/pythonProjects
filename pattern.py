'''
 reset() - Erase all of the patterns and start over
 setup()
Configure turtle to draw quickly
Configure turtle to have a window of 1000 x 800
 drawRectanglePattern()
Use appropriate parameters
See additional information below
It should call drawRectangle()
drawRectangle()
Use appropriate parameters
Should draw a SINGLE rectangle
drawCirclePattern()
Use appropriate parameters
See additional information below
drawSuperPattern()
Use appropriate parameters
Randomly draw Rectangle and Circle patterns. Each pattern should based on random values.
Use reasonable random values (some can be negative) so patterns are drawn on the screen
setRandomColor()
Do not use any parameters
Set turtle to draw in a random color
Use at least 4 colors
done()
Called when user quits
Keeps the turtle window open
Make sure to read the rubric to see the additional requirements.

Drawing Rectangle Pattern
The Rectangle Pattern has 6 parts to it

Center position - This is the x, y center point of the circular pattern that is drawn
Offset - This is the distance from the center position to the starting corner of each rectangle. It can be a positive or negative number
Height - The height of a rectangle
Width - The width of a rectangle
Count - The number of rectangles to draw within the 360 degree pattern.
Rotation - The number of degrees each rectangle is rotated in relation to the line from the Center Position to the starting corner of the rectangle
Each individual rectangle should be a new random color. You should use at least 4 different colors.

Drawing Circle Pattern
The Circle Pattern has 4 parts to it

Center position - This is the x, y center point of the circular pattern that is drawn
Offset - This is the distance from the center position to starting drawing point of each circle.  It can be a positive or negative number. Note that the center point of each circle should be 'radius + offset' distance from the Center Position of the pattern.
Radius - The radius of the circle
Count - The number of circles to draw within the 360 degree pattern.
Each individual circle should be a new random color. You should use at least 4 different colors.
'''
import turtle as t
import math

def reset():
    pass

def setup():
    pass

def drawRectanglePattern(x,y,o,w,h,c,r):
    t.speed(100)
    th = 360/c
    for i in range(0,c):
        offsetx = math.cos(math.radians(th*(i)))*o
        offsety = math.sin(math.radians(th*(i)))*o
        t.penup()
        t.goto(x+(offsetx),y+(offsety))
        t.pendown()
        drawRectangle(w,h,r)
    pass

def drawRectangle(w,h,r):
    t.forward(w)
    t.left(90)
    t.forward(h)
    t.left(90)
    t.forward(w)
    t.left(90)
    t.forward(h)
    t.left(90)

def drawCirclePattern():
    pass

def drawCircle():
    pass

def drawSuperPattern():
    pass

drawRectanglePattern(50,50,100,30,40,100,30)
