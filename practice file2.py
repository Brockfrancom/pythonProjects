
"""
# Check whether a solution is valid
def isValid(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] < 1 or grid[i][j] > 9 \
               or not isValidAt(<YOUR CODE HERE>):
                return False
    return True # The fixed cells are valid

# Check whether grid[i][j] is valid in the grid
def isValidAt(i, j, grid):
    # Check whether grid[i][j] is valid in i's row
    <YOUR CODE HERE>

    # Check whether grid[i][j] is valid in j's column
    <YOUR CODE HERE>

    # Check whether grid[i][j] is valid in the 3-by-3 box
    <YOUR CODE HERE>

    return True # The current value at grid[i][j] is valid
"""
"""
from tkinter import *

def press(*args):
    print('press')
    global pressed
    pressed = True
    master.after(0, loop)

def release(*args):
    print('release')
    global pressed
    pressed = False

def loop():
    if pressed:
        print('loop')
        # Infinite loop without delay is bad idea.
        master.after(250, loop)

master = Tk()
pressed = False

b = Button(master, text="OK")
b.bind("<Button-1>", press)
b.bind("<ButtonRelease-1>", release)
b.pack()
mainloop()
"""
"""
from tkinter import * 

class WidgetsDemo:
    def __init__(self):
        window = Tk() 
        window.title("Widgets Demo") 

        frame1 = Frame(window)  
        frame1.pack()

        self.v1 = IntVar()
        cbtBold = Checkbutton(frame1, text="Bold", variable = self.v1, command = self.processCheckbutton)

        self.v2 = IntVar()
        rbRed = Radiobutton(frame1, text="Red", bg="red", value=3, variable = self.v2, command = self.processRadiobutton)
        rbYellow = Radiobutton(frame1, text="Yellow", bg="yellow", value=2, variable = self.v2, command = self.processRadiobutton)

        cbtBold.grid(row=1, column=1)
        rbRed.grid(row=1, column=2)
        rbYellow.grid(row=1, column=3)

        frame2 = Frame(window)  
        frame2.pack()
        label = Label(frame2, text="Enter your name: ")

        self.name = StringVar()
        entryName = Entry(frame2, textvariable = self.name)
        btGetName = Button(frame2, text="Get Name", command = self.processButton)
        self.message = Message(frame2, text="It is a widgets demo")

        label.grid(row = 1, column = 1)
        entryName.grid(row = 1, column = 2)
        btGetName.grid(row = 1, column = 3)
        self.message.grid(row = 1, column = 4)

        text = Text(window) 
        text.pack()
        text.insert(END, "Tip\nThe best way to learn Tkinter is to read ")
        text.insert(END, "these carefully designed examples and use them ")
        text.insert(END, "to create your applications.")

        window.mainloop() 

    def processCheckbutton(self):
        # Replace <YOUR CODE HERE> with the value of self.v1
        print("check button is " + ("checked " if self.v1.get() == 1 else "unchecked"))

    def processRadiobutton(self):
        print(("Red" if self.v2.get() == 3 else "Yellow") + " is selected ")

    def processButton(self):
        self.message["text"] = self.name.get()

WidgetsDemo()

"""
myList = [1, 2, 3, 4, 5, 6]
for i in range(1, 6):
    myList[i - 1] = myList[i]

for i in range(0, 6): 
    print(myList[i], end = " ")

    
    
    
    
    
    
    
    
    
    