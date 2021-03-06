

# Check whether a solution is valid
def isValid(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] < 1 or grid[i][j] > 9 \
               or not isValidAt(i, j, grid):
                return False
    return True # The fixed cells are valid

# Check whether grid[i][j] is valid in the grid
def isValidAt(i, j, grid):
    # Check whether grid[i][j] is valid in i's row
    for k in range(9):
        if k != j and grid[i][k] == grid[i][j]:
            return False
    # Check whether grid[i][j] is valid in j's column
    for l in range(9):
        if l != i and grid[l][j] == grid[i][j]:
            return False
    # Check whether grid[i][j] is valid in the 3-by-3 box
    for row in range((i // 3)*3, (i // 3)*3 + 3):
        for col in range((j // 3)*3, (j // 3)*3 + 3):
            if row != i and col != j and grid[row][col] == grid[i][j]:
                return False
        

    return True # The current value at grid[i][j] is valid

















