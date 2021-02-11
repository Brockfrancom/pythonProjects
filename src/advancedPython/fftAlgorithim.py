import math
from cmath import exp, pi
import numpy as np
import random
import time
import matplotlib.pyplot as plt

'''
P: Array of coefficents (complex numbers)
P: [ Complex(v,0), ...]
x: values of Omega(w)
n: size    
'''
def FFT(P, x, n):
    if n==1:
        return P
    #Split into even/odd
    E = P[0::2]
    O = P[1::2]
    #loop through values in x Square values in x (1/2 only)
    x2 = [x[i]*x[i] for i in range(0, n//2)]
    #Call FFT recursivly for even, then odd 
    SE = FFT(E, x2, n//2)
    SO = FFT(O, x2, n//2)
    #construct solution
    first= [SE[i]+x2[i]*SO[i] for i in range(0, n//2)]
    second= [SE[i]-x2[i]*SO[i] for i in range(0, n//2)]
    return first + second
    
def getV(n, m):
    if m == 1:
        comp = [complex(math.sin(i*(2*pi/n)), math.cos(2*pi*(i/n))) for i in range(0, n)]
    else:
        comp = [(complex(math.sin(i*(2*pi/n)), math.cos(2*pi*(i/n)))).conjugate() for i in range(0, n)]
    return comp

'''
n = 8
p = [0, 1, 2, 3, 4, 5, 6, 7]
#p = [15, 21, 13, 44] 
print("Forward FFT")
sol=FFT([complex(p[i],0) for i in range(0,n)], getV(n, 1), n)
print(sol)
print("Inverse FFT")
back=FFT(sol, getV(n, -1), n)
for i in range(0, len(back)):
    back[i] = back[i]/n
print(back)
print()
and the answer back is:

[1.1102230246251565e-16j, 
(1-1.6653345369377348e-16j), 
(2+3.2162452993532727e-16j), 
(3.0000000000000004+1.6653345369377348e-16j), 
(4-1.1102230246251565e-16j), 
(5-1.6653345369377348e-16j), 
(6-3.2162452993532727e-16j), 
(7+1.6653345369377348e-16j)]

These results are the same within 15 significant digits.
'''
def run():
    number = []
    FFTresults = []
    i = 128
    while(i <= 67108864):
        print("Running simulation: "+str(i))
        number.append(i)
        p = [random.randint(0, i) for x in range(0, i)]
        start = time.time()
        A = FFT([complex(p[n],0) for n in range(0,i)], getV(i, 1), i)
        total = time.time() - start
        FFTresults.append(total)
        i = 2*i
    
    plt.plot(FFTresults, number, 'r', label='FFT')
    plt.xlabel("Run time, seconds")
    plt.ylabel("Number of elements")
    plt.title("Polynomial multipy, FFT algorithim")
    plt.legend()
    plt.show()
