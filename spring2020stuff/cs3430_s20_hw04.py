####################################
# module: cs3430_s20_hw04.py
# Brock Francom
# A02052161
####################################
import numpy as np

### ============== Problem 1 ==================
def simplex(tab):
    """
    Apply the simplex algorithm to the tableaue tab.
    Returns None if there is no solution.
    """
    in_vars, m = tab[0], tab[1]
    nr, nc = m.shape
    minVal = 0 
    column = 0
    for i in range(0, nc-1): # ignore B.S column
        if m[nr-1][i] < minVal:
            minVal = m[nr-1][i]
            column = i
    if minVal == 0: #there are no negative values in the p row
        return (in_vars, m)
    minQuotient = 99999999999999999999
    row = 0
    for i in range(0, nr-1): #Ignore the p row
        val = m[i][column]
        if val > 0:
            quotient = m[i][nc-1]/val
            if quotient < minQuotient:
                minQuotient = quotient
                row = i
    if minQuotient == 99999999999999999999: #No positive entry in entering col.
        return None
    pivot = m[row][column]
    in_vars[row] = column #update the invars
    m[row,:] = (1/pivot)* m[row,:] #pivot to 1
    for i in range(0, nr):
        if i != row:
            m[i,:] = m[i,:] - ((m[i][column])* m[row,:])
    return simplex((in_vars, m))        
    
def get_solution_from_tab(tab):
    in_vars, mat = tab[0], tab[1]
    nr, nc = mat.shape
    sol = {}
    for k, v in in_vars.items():
        sol[v] = mat[k,nc-1]
    sol['p'] = mat[nr-1,nc-1]
    return sol

def display_solution_from_tab(tab):
    sol = get_solution_from_tab(tab)
    for var, val in sol.items():
        if var == 'p':
            print('p\t=\t{}'.format(val))
        else:
            print('x{}\t=\t{}'.format(var, val))

### =============== Problem 2 ====================
def problem_2_1():
    ### replace tab with your definitions
    ### for Problem 2.1
    in_vars = {0:2, 1:3} 
    m = np.array([[  3,  8,  1,  0, 24],
                  [  6,  4,  0,  1, 30],
                  [ -2, -3,  0,  0,  0]],
                 dtype=float)   
    tab = (in_vars, m)
    tab = simplex(tab)
    if tab == None:
        print("No solution.")
        return    
    print('solved={}'.format(tab[1]))
    display_solution_from_tab(tab)

def problem_2_2():
    ### replace tab with your definitions
    ### for Problem 2.2.
    in_vars = {0:2, 1:3} 
    m = np.array([[  1, -1,  1,  0,  4],
                  [ -1,  3,  0,  1,  4],
                  [ -1,  0,  0,  0,  0]],
                 dtype=float)   
    tab = (in_vars, m)
    tab = simplex(tab)
    if tab == None:
        print("No solution.")
        return    
    print('solved={}'.format(tab[1]))
    display_solution_from_tab(tab)

def problem_2_3():
    ### replace tab with your definitions
    ### for Problem 2.3.
    in_vars = {0:3, 1:4, 2:5} 
    m = np.array([[  12,  6,   0,  1,  0,  0,  1500],
                  [  18, 12,  10,  0,  1,  0,  2500],
                  [  15,  8,   0,  0,  0,  1,  2000],
                  [-1.5,-.8,-.25,  0,  0,  0,  0]],
                 dtype=float)   
    tab = (in_vars, m)
    tab = simplex(tab)
    if tab == None:
        print("No solution.")
        return    
    print('solved={}'.format(tab[1]))
    display_solution_from_tab(tab)

def problem_2_4():
    ### replace tab with your definitions
    ### for Problem 2.4.
    in_vars = {0:2, 1:3} 
    m = np.array([[   1,  1,   1,  1,  0,  1000],
                  [   .5,  1/3,   1/3,  0,  1,  600],
                  [-120,-96,-100,  0,  0,  0]],
                 dtype=float) 
    tab = (in_vars, m)
    tab = simplex(tab)
    if tab == None:
        print("No solution.")
        return    
    print('solved={}'.format(tab[1]))
    display_solution_from_tab(tab)

####################### Testing problem 1 ######################
'''
in_vars = {0:3, 1:4, 2:5} 
m = np.array([[20,4,4,1,0,0,6000],
              [8,8,4,0,1,0,10000],
              [8,4,2,0,0,1,4000],
              [-3,-8,-6,0,0,0,0]],
              dtype=float)   

tab1 = (in_vars, m)
tab = simplex(tab1)
display_solution_from_tab(tab)
'''
problem_2_1()
print()
problem_2_2()
print()
problem_2_3()
print()
problem_2_4()
