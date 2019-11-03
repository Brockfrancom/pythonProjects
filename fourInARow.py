"""
Brock Francom
A02052161
CS-1400-001
Douglas Galarus
4/10/2018
hw12 - Exercise 11.19

NOTE: To use file redirection, use a file named "input1.txt" or change the file
name in the script. The file should be entered one number per line with the 
first line corresponding to # of rows, and the second line to # of columns, 
followed by the matrix values.

"""

#function to create a matrix by the user entering the numbers manually one per 
#line seperated by enter.
def readMatrix():
    global nRows
    global nCols
    nRows = eval(input("Enter the number of rows: "))
    nCols = eval(input("Enter the number of columns: "))
    matrix = [] 
    for r in range(nRows):
        matrix.append([]) # Add an empty new row
        for c in range(nCols):
            value = input("Enter an element and press Enter: ")
            matrix[r].append(value)
    return matrix

#function to read a file named "input1.txt". The file should be entered one 
#number per line with the first line corresponding to # of rows, and the 
#second line to # of columns, and create a matrix with the remaining numbers.
def readAFile():
    global nRows
    global nCols
    file = open("TestGrid.txt") #open file "input1.txt"
    nRows = eval(file.readline().strip()) #read # of rows in fist line
    nCols = eval(file.readline(2).strip()) #read # of columns in second line
    matrix = []
    for row in range(nRows):
        matrix.append([]) # add an empty new row
        for _ in range(nCols):
            value = eval(file.readline(3).strip()) #read the file starting with line 3
            matrix[row].append(value) #append value to matrix
    return matrix

#function to check the rows
def checkRows(nRows, nCols, board):
    for i in range(nRows):
        count = 1
        for j in range(nCols - 1):
            if board[i][j] == board[i][j + 1]: #check for equality to right
                count += 1 #increase count if same value
            else:
                count = 1 #reset if not the same
            if count == 4: #return if 4 in a row
                return True
    return False

#function to check the columns
def checkCols(nRows, nCols, board):
    for j in range(nCols):
        count = 1
        for i in range(nRows - 1):
            if board[i][j] == board[i + 1][j]: #check for equality down
                count += 1 #increase count if same value
            else:
                count = 1 #reset if not the same
            if count == 4: #return if 4 in a row
                return True
    return False

#function to check diagonals down and right
def checkDiag1(nRows, nCols, board):
    for i in range(nRows - 3):
        count = 1
        for j in range(nCols - 3):
            if board[i][j] == board[i + 1][j + 1]: #check for equality diagonal
                count += 1 #increase count if same value
            else:
                count = 1 #reset if not the same
                break
            if board[i + 1][j + 1] == board[i + 2][j + 2]: #check for equality diagonal
                count += 1 #increase count if same value
            else:
                count = 1 #reset if not the same
                break
            if board[i + 2][j + 2] == board[i + 3][j + 3]: #check for equality diagonal
                count += 1 #increase count if same value
            else:
                count = 1 #reset if not the same
                break
            if count == 4: #return if 4 in a row
                return True
    return False

#function to check diagonals down and left
def checkDiag2(nRows, nCols, board):
    for i in range(0, nRows - 3):
        count = 1
        for j in range(nCols - 1, 2, -1):
            if board[i][j] == board[i + 1][j - 1]: #check for equality diagonal
                count += 1 #increase count if same value
            else:
                count = 1 #reset if not the same
                break
            if board[i + 1][j - 1] == board[i + 2][j - 2]: #check for equality diagonal
                count += 1 #increase count if same value
            else:
                count = 1 #reset if not the same
                break
            if board[i + 2][j - 2] == board[i + 3][j - 3]: #check for equality diagonal
                count += 1 #increase count if same value
            else:
                count = 1 #reset if not the same
                break
            if count == 4: #return if 4 in a row
                return True
    return False

#this is the main function, it calls 4 other checks and returns true or false 
def isConsecutiveFour(nRows, nCols, board):
    if checkRows(nRows, nCols, board) or checkCols(nRows, nCols, board) or \
    checkDiag1(nRows, nCols, board) or checkDiag2(nRows, nCols, board):
        print("True")
    else:
        print("False")
   
# Use this to read a set of numbers one per line from a file via file 
# redirection.
board = readAFile()

#board = readMatrix() # Uncomment this line to enter a set of numbers manually 
                      # seperated by enter

#call the main function
isConsecutiveFour(nRows, nCols, board)



print(checkDiag2(nRows, nCols, board))












