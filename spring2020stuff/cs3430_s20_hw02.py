#################################################
# Module: cs3430_s20_hw02.py
# Brock Francom
# A02052161
# bugs to vladimir dot kulyukin at usu dot edu
#################################################
import numpy as np
import pickle

def comp_2d_mats(a, b, err=0.0001):
    """
    Compare two matrices a and b. Returns true if
    a and b are of the same shape and, for every
    legitimate position (i, j), abs(a[i][j] - b[i][j]) <= err.
    """
    ra, ca = a.shape
    rb, cb = b.shape
    if ra != rb:
        return False
    if ca != cb:
        return False
    for r in range(ra):
        for c in range(ca):
            if abs(a[r][c] - b[r][c]) > err:
                return False
    return True

def lu_decomp(a, n):
    """ 
    lu_decomp(a, n) returns u, l such that np.dot(l, u) === a.
    a is an nxn matrix that is reduced to the upper and lower triangular matrices. 
    throws exception when there is no pivot in a column or rows must be swapped
    to create a pivot.
    lu_decomp(a, n) is destructive in that a is destructively modified into u.
    """
    u = a.copy()
    l = np.eye(n, n) 
    #Put matrix into upper form
    for c in range(0, n):
        for r in range(c, n):
            if r != c:
                m=u[r][c]/u[c][c]
                u[r,:] = u[r,:]-(m*u[c,:])
                l[r][c] = m
            else:
                if u[r][c] == 0:
                    temp = u[r,:].copy()
                    if ((r+1) < n):
                        u[r,:] = u[(r+1),:]
                        u[r+1,:] = temp
                    else:
                        return None
    return u, l

def check_lin_sys_sol(a, n, b, m, x, err=0.0001):
    ra, ca = a.shape
    assert ra == n
    assert ca == n
    assert b.shape[0] == n
    assert b.shape[1] == m
    assert b.shape == x.shape
    for c in range(m):
        bb = np.array([np.matmul(a, x[:,c])]).T
        for r in range(n):
            assert abs(b[r][c] - bb[r][0]) <= err

def test_lud_solve(a, n, b, m, err=0.0001, prnt_flag=True):
    x = lud_solve(a, n, b, m)   
    check_lin_sys_sol(a, n, b, m, x, err=err)
    if prnt_flag:
        print('A:')
        print(a)
        print('b:')
        print(b)
        print('x:')
        print(x)
        print('A*x:')
        print(np.dot(a, x))

def test_lud_solve2(a, n, b, m, err=0.0001, prnt_flag=True):
    aa = a.copy()
    u, l = lu_decomp(aa, n)
    bb = b.copy()
    x = lud_solve2(u, l, n, bb, m)
    check_lin_sys_sol(a, n, b, m, x, err=err)
    if prnt_flag:
        print('A:')
        print(a)
        print('b:')
        print(b)
        print('x:')
        print(x)
        print('A*x:')
        print(np.dot(a, x))

def bsubst(a, n, b, m):
    """
    bsubst uses back substitution to solve ax = b1, b2, ..., bm.
    a is an nxn upper-triangular matrix, n is its dimension.
    b is an nxm matrix of vectors b1, b2, ..., bm. 
    returns x.
    """
    answer = b.copy()
    for r in range(n-1, -1, -1):
        for c in range(r+1,n):
            b[r] = b[r] - (a[r,c]*answer[c])
        answer[r] = b[r]/a[r,r]
    #answer is now the solution to ax = b
    return answer

def fsubst(a, n, b, m):
    """
    fsubst uses forward substitution to solve ax = b1, b2, ..., bm.
    a is an nxn lower-triangular matrix, n is its dimension.
    b is an nxm matrix of vectors b1, b2, ..., bm.
    returns x.
    """
    answer = b.copy()
    for r in range(0, n, 1):
        for c in range(0,r+1):
            b[r] = b[r] - (a[r,c]*answer[c])
        answer[r] = b[r]/a[r,r]
    #answer is now the solution to ax = b
    return answer

def lud_solve(a, n, b, m):
    """
    a is an nxn matrix; b is m nx1 vectors.
    Use forward subst to solve Ly = b for y.
    Use back    subst to solve Ux = y for x.
    Then LUx = Ly = b.
    Returns x.
    """
    u = a.copy()
    bb = b.copy()
    L = np.eye(n, n) 
    #Put matrix into upper form
    for c in range(0, n):
        for r in range(c, n):
            if r != c:
                m=u[r][c]/u[c][c]
                u[r,:] = u[r,:]-(m*u[c,:])
                bb[r] = bb[r] - (m*bb[c])
                L[r][c] = m
            else:
                if u[r][c] == 0:
                    temp = u[r,:].copy()
                    tempb = bb[r].copy()
                    if ((r+1) < n):
                        u[r,:] = u[(r+1),:]
                        u[r+1,:] = temp
                        bb[r,:] = bb[(r+1),:]
                        bb[r+1,:] = tempb
                    else:
                        return None
    answer = bsubst(u, n, bb, m)                    
    return answer

def lud_solve2(u, l, n, b, m):
    """
    Uses L to transform b to c.
    Then backsubst to solve Ux = c for x.
    Returns x.
    """
    bb = b.copy()
    for c in range(0, n):
        for r in range(0, n):
            if c<r:
                bb[r] = bb[r] - (l[r][c]*bb[c])
    answer = bsubst(u, n, bb, m)                    
    return answer

def load_lin_systems(file_name):
    with open(file_name, 'rb') as fp:
        return pickle.load(fp)

def test_lud_solve_on_lin_systems(file_name, err=.0001):
    print('Testing LUD on {} ...'.format(file_name))
    lu_problems = []
    lin_systems = load_lin_systems(file_name)
    for A, b in lin_systems:
        try:
            test_lud_solve2(A, A.shape[0], b, 1, err=err, prnt_flag=False)
        except AssertionError:
            print()
            print("Assertion error for A:")
            print(A)
            print()
            print(b)
            lu_problems.append((A, b))
        except Exception as e:
            print(e)
            lu_problems.append((A, b))
    print('{} LUD solve failures out of {}'.format(len(lu_problems), len(lin_systems)))

if __name__ == '__main__':
    test_lud_solve_on_lin_systems('ab_100x100.pck')
    

