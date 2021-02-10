####################################
# module: rmb.py
# YOUR NAME
# YOUR A#
####################################

import numpy as np

class rmb(object):
   
    @staticmethod
    def rjl(f, a, b, j, l):
        c = np.zeros((j+1, l+1), dtype=np.longdouble)
        for i in range(1,j+1):
            c[i,1] = trapezoidal(f, a, b, 2**(i-1))
        for m in range(2, l+1):
            for k in range(1, j+1):
                t1 = c[k,m-1]
                t2 = c[k-1,m-1]
                div = (4.0**(np.longdouble(m-1.0)))-1.0
                c[k,m] = t1 + ((t1 - t2)/(div))
        return c[j,l]

def trapezoidal(f, a, b, n):
    h = float(b - a) / n
    s = 0.0
    s += h * f(a)
    for i in range(1, n):
        s += 2.0 * h * f(a + i*h)
    s += h * f(b)
    return s/2.0
