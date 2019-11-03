"""
Brock Francom
A02052161
CS-1400-001
Douglas Galarus
4/10/2018
hw12 - Exercise 11.36
"""
import turtle
import random

#draw a grid
turtle.speed(50)
turtle.color("gray")
x = -80
for y in range(-80,80 + 1, 10):
    turtle.penup()    
    turtle.goto(x,y)
    turtle.pendown()
    turtle.forward(160)
    turtle.penup()
y = 80
turtle.right(90)
for x in range(-80,80 + 1, 10):
    turtle.penup()    
    turtle.goto(x,y)
    turtle.pendown()
    turtle.forward(160)
    turtle.penup()
#change colors to draw the walk
turtle.pensize(3)
turtle.color('red')
turtle.home()
turtle.pendown()
turtle.speed(1)
#create a matrix with the starting point and set starting values of x and y to 0
matrix = [0,0]
x = y = 0
#walking
while abs(x) < 80 and abs(y) < 80:
    var = random.randint(0,3)   
    #randomly walk 
    if var == 0:
        x += 10
        matrix.append([x,y]) #add point to list
        if matrix.index([x, y]) == len(matrix) - 1:
            turtle.goto(x,y) #if the point isnt in the list, go to the point.
        else:
            matrix.pop() #remove the point, and pick a different point
            x -= 10
            y += 10
            matrix.append([x,y])
            if matrix.index([x, y]) == len(matrix) - 1:
                turtle.goto(x,y) #if not in the list, go to point
            else:
                matrix.pop() #remove the point, and pick a different point
                y -= 20
                matrix.append([x,y])
                if matrix.index([x, y]) == len(matrix) - 1:
                    turtle.goto(x,y) #if not in the list, go to point
                else:
                    matrix.pop() #remove the point, and pick a different point
                    y += 10
                    x -= 10
                    matrix.append([x,y])
                    if matrix.index([x, y]) == len(matrix) - 1:
                        turtle.goto(x,y)#if not in the list, go to point
                    else:
                        break #end the program if no more options. 
    #the comments are the same for the next if else statements.
    elif var == 1:   
        y -= 10
        matrix.append([x,y])
        if matrix.index([x, y]) == len(matrix) - 1:
            turtle.goto(x,y)
        else:
            matrix.pop()
            y += 10
            x += 10
            matrix.append([x,y])
            if matrix.index([x, y]) == len(matrix) - 1:
                turtle.goto(x,y)
            else:
                matrix.pop()
                x -= 20
                matrix.append([x,y])
                if matrix.index([x, y]) == len(matrix) - 1:
                    turtle.goto(x,y)
                else:
                    matrix.pop()
                    x += 10
                    y += 10
                    matrix.append([x,y])
                    if matrix.index([x, y]) == len(matrix) - 1:
                        turtle.goto(x,y)
                    else:
                        break
    elif var == 2:
        x -= 10
        matrix.append([x,y])
        if matrix.index([x, y]) == len(matrix) - 1:
            turtle.goto(x,y)
        else:
            matrix.pop()
            x += 10
            y += 10
            matrix.append([x,y])
            if matrix.index([x, y]) == len(matrix) - 1:
                turtle.goto(x,y)
            else:
                matrix.pop()
                y -= 20
                matrix.append([x,y])
                if matrix.index([x, y]) == len(matrix) - 1:
                    turtle.goto(x,y)
                else:
                    matrix.pop()
                    y += 10
                    x += 10
                    matrix.append([x,y])
                    if matrix.index([x, y]) == len(matrix) - 1:
                        turtle.goto(x,y)
                    else:
                        break
    elif var == 3:
        y += 10
        matrix.append([x,y])
        if matrix.index([x, y]) == len(matrix) - 1:
            turtle.goto(x,y)
        else:
            matrix.pop()
            y -= 10
            x += 10
            matrix.append([x,y])
            if matrix.index([x, y]) == len(matrix) - 1:
                turtle.goto(x,y)
            else:
                matrix.pop()
                x -= 20
                matrix.append([x,y])
                if matrix.index([x, y]) == len(matrix) - 1:
                    turtle.goto(x,y)
                else:
                    matrix.pop()
                    x += 10
                    y -= 10
                    matrix.append([x,y])
                    if matrix.index([x, y]) == len(matrix) - 1:
                        turtle.goto(x,y)
                    else:
                        break

turtle.done




