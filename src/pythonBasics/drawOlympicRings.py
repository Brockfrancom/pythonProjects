"""
Brock Francom
A02052161
CS-1400-001
Douglas Galarus
2/1/2018
hw Exercise 3.14
"""

def run():
    #get user input
    radius = eval(input("Enter a value for radius: "))
    
    #turtle
    import turtle
    
    #circle1
    turtle.circle(radius)
    turtle.penup()
    
    #circle2
    turtle.backward(radius * 2.5)
    turtle.color("blue")
    turtle.pendown()
    turtle.circle(radius)
    turtle.penup()
    
    #circle3
    turtle.forward(radius * 5)
    turtle.color("red")
    turtle.pendown()
    turtle.circle(radius)
    turtle.penup()
    
    #circle4
    turtle.home()
    turtle.backward(radius * 1.25)
    turtle.right(90)
    turtle.forward(radius)
    turtle.left(90)
    turtle.color("yellow")
    turtle.pendown()
    turtle.circle(radius)
    turtle.penup()
    
    #circle5
    turtle.home()
    turtle.forward(radius * 1.25)
    turtle.right(90)
    turtle.forward(radius)
    turtle.left(90)
    turtle.color("green")
    turtle.pendown()
    turtle.circle(radius)
    
    turtle.done()
    turtle.mainloop()