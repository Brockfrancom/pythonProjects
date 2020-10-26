"""
Brock Francom
A02052161
CS-1400-001
Douglas Galarus
1/24/2018
hw3 - 3-2-25

2.25 (Turtle: draw a rectangle) Write a program that prompts the user to enter
 the center of a rectangle, width, and height, and displays the rectangle, as 
 shown in Figure 2.4c in our textbook.

"""

def run():
    #get point (x,y), height, width from user
    x = eval(input("Enter the x coordinate for the center of the rectangle: "))
    y = eval(input("Enter the y coordinate for the center of the rectangle: "))
    width = eval(input("Enter a width for the rectangle: "))
    height = eval(input("Enter a height for the rectangle: "))
    
    #calculate turtle start point
    x1 = (x - (width / 2))
    y1 = (y + (height / 2))
    
    #turtle
    import turtle
    
    #go to start
    turtle.penup()
    turtle.goto(x1,y1)
    turtle.pendown()
    
    #draw rectangle
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    
    turtle.done()
    turtle.mainloop()
















