"""
Brock Francom
A02052161
CS-1400-001
Douglas Galarus
4/17/2018
hw13 - Exercise 9.20

NOTE:
The message will be displayed after the left mouse button is clicked and held, 
and the mouse is moved. The message will continue to be displayed until the 
button is released, which is what I assumed from the problem discription.

"""

from tkinter import *
import math

#function to delete text when left mouse button is released
def release(event):
    canvas.delete(Y, N)
    
#function to determine if the pointer is in the circle and display message
def processEvent(event):
    a = event.x - 100
    b = event.y - 60  
    c = math.sqrt((a ** 2) + (b ** 2))
    if c <= 50:
        canvas.delete(Y, N) #deletes the previous message
        canvas.create_text(event.x, event.y, text = "Mouse pointer is in the "\
                           "circle", tags = Y)
    else:
        canvas.delete(Y, N) #deletes the previous message
        canvas.create_text(event.x, event.y, text = "Mouse pointer is not in "\
                           "the circle", tags = N)

window = Tk() #create a window
canvas = Canvas(window) #add a canvas
canvas.pack()

#create a circle on the canvas
c1 = canvas.create_oval(50, 10, 150, 110)

#button events
canvas.bind("<B1-Motion>", processEvent)
canvas.bind("<ButtonRelease-1>", release)


window.mainloop()

