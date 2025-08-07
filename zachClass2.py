import turtle as t

def drawChessboard(startX, startY, w=250, h=250):
    t.speed(500)
    t.penup()
    t.goto(startX, startY)
    t.pendown()
    t.forward(w)
    t.left(90)
    t.forward(h)
    t.left(90)
    t.forward(w)
    t.left(90)
    t.forward(h)
    t.left(90)
    drawAllRectangles(t,startX, startY, w/8, h/8)
    t.done()

def drawAllRectangles(t,startX, startY, w1, h1):
    for i in range(0,8,2):
        for j in range(0,8,2):
            t.penup()
            t.goto((startX)+(i*w1),(startY)+(j*h1))
            t.pendown()
            drawRectangle(t,w1,h1)
    for i in range(0,8,2):
        for j in range(0,8,2):
            t.penup()
            t.goto((startX)+((i+1)*w1),(startY)+((j+1)*h1))
            t.pendown()
            drawRectangle(t,w1,h1)

def drawRectangle(t,w1,h1):
    t.fillcolor("black")
    t.begin_fill()
    t.forward(w1)
    t.left(90)
    t.forward(h1)
    t.left(90)
    t.forward(w1)
    t.left(90)
    t.forward(h1)
    t.left(90)
    t.end_fill()

if __name__=="__main__":
    startX = 5
    startY = 5
    width = "200"
    height = "200"
    if width == "" and height == "":
        drawChessboard(startX, startY)
    elif height == "":
        drawChessboard(startX, startY, width=eval(width))
    elif width == "":
        drawChessboard(startX, startY, height=eval(height))
    else:
        drawChessboard(startX, startY, eval(width), eval(height))
