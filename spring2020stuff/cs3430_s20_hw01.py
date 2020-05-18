######################################################
# module: cs3430_s20_hw01.py
# Brock Francom
# A02052161
######################################################

import numpy as np
import numpy.linalg
import random

### ============= Problem 1 (Gauss-Jordan Elimination) ===============
def gje(a, b):
    """ Gauss-Jordan Elimination to solve Ax = b. """
    nc, nr = a.shape
    answer = b.copy() # This will become the solution to ax = b
    #Put matrix into upper form
    for j in range(0, nc):
        for i in range(j, nr):
            if i != j:
                m=a[i][j]/a[j][j]
                a[i,:] = a[i,:]-(m*a[j,:])
                b[i] = b[i] - (m*b[j])
            else:
                if a[i][j] == 0:
                    temp = a[i,:]
                    if i+1 <= nc -1:
                        a[i,:] = a[i+1,:]
                        a[i+1,:] = temp
                        
    #the matrix a is now in upper triangle form, U
    #The column vector b is now y?
    #Back substitute                                     
    for row in range(nr-1, -1, -1):
        for col in range(row+1,nr):
            b[row] = b[row] - (a[row,col]*answer[col])
        answer[row] = b[row]/a[row,row]
    #answer is now the solution to ax = b
    return answer

## ============== Problem 2 (Determinant) ========================

def random_mat(nr, nc, lower, upper):
    """ Generate an nrxnc matrix of random numbers in [lower, upper]. """
    m = np.zeros((nr, nc))
    for r in range(nr):
        for c in range(nc):
            m[r][c] = random.randint(lower, upper)
    return m

def leibniz_det(a):
    """ Compute determinant of nxn matrix a with Leibniz formula. """
    nr, nc = a.shape
    det = 0
    if nc==nr==2:
        return ((a[0][0] * a[1][1]) - (a[0][1] * a[1][0]))
    for j in range(0, nc):
        for i in range(j, nr):
            b = np.delete(a,np.s_[j:j+1], axis=1)
            b = np.delete(b,np.s_[i:i+1], axis=0)
            det += (a[i][j] * (((-1)**(i+j)) * leibniz_det(b)))
        break
    return det

def gauss_det(a):
    """ Compute determinant of nxn matrix a with Gaussian elimination. """
    U, rowExchanges = gjeUpperForm(a)
    nr, nc = U.shape
    productOfPivots = 1
    for j in range(0, nc):
        for i in range(0, nr):
            if i==j:
                if U[i,j] != 0:
                    productOfPivots = productOfPivots * U[i,j]
        
    determinant = ((-1)**rowExchanges)*(productOfPivots)
    return determinant

#Helper method to calculate a gaussian determinant
def gjeUpperForm(a):
    nc, nr = a.shape
    #Put matrix into upper form, counting row exchanges
    rowExchanges = 0
    for j in range(0, nc):
        for i in range(j, nr):
            if i != j:
                m=a[i][j]/a[j][j]
                a[i,:] = a[i,:]-(m*a[j,:])
            else:
                if a[i][j] == 0:
                    temp = a[i,:]
                    if i+1 <= (nc -1):
                        a[i,:] = a[i+1,:]
                        a[i+1,:] = temp
                        rowExchanges += 1
    return a, rowExchanges

## ============== Problem 3 (Cramer's Rule) ======================

def cramer(A, b):
    """ Solve Ax = b with Cramer's Rule. """
    detA = np.linalg.det(A)
    x = b.copy()    
    for col in range(A.shape[1]):
        B = np.delete(A,np.s_[col:col+1], axis=1)
        B = np.insert(B,[col],b,axis=1)
        detB = np.linalg.det(B)
        x[col] = detB/detA
    return x

if __name__ == '__main__':
    A = np.array(
        [[2, -1, 3],
         [3, 0, 2],
         [-2, 1, 4]],
        dtype=float)
    
    b = np.array([[4],
                  [5],
                  [6]],
                 dtype=float)
        
    answer = gje(A, b)
    print("Gauss-Jordan solution to Ax=b:")
    print(answer)
    print()
    
    A1 = np.array([[2., 1., 0., 1.],
                   [3., 2., 1., 2.],
                   [4., 0., 1., 4.],
                   [1., 0., 2., 1.]])
    
    answer = leibniz_det(A1)
    print("Leibniz Determinant of A1:")
    print(answer)
    print()
    
    A1 = np.array([[2., 1., 0., 1.],
                   [3., 2., 1., 2.],
                   [4., 0., 1., 4.],
                   [1., 0., 2., 1.]])

    answer = gauss_det(A1)
    print("Gaussian Determinant of A1:")
    print(answer)
    print()
    
    A1 = np.array([[2., 1., 0., 1.],
                   [3., 2., 1., 2.],
                   [4., 0., 1., 4.],
                   [1., 0., 2., 1.]])

    print("Linalg determinant of A1:")
    print(np.linalg.det(A1))
    print()
    
    A = np.array(
        [[2, -1, 3],
         [3, 0, 2],
         [-2, 1, 4]],
        dtype=float)
    
    b = np.array([[4],
                  [5],
                  [6]],
                 dtype=float)
    
    print("Cramers rule of Ax = b:")
    print(cramer(A, b))

    
