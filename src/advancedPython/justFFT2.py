'''
Brock Francom
A02052161
Assignment 10 
'''
import numpy as np
import random
import time
import matplotlib.pyplot as plt
from math import *
import math

def polyMultFFT(N0, N1):
    '''
    This funciton is a wrapper used to perform a multiplication of polynomials with the 
    FFT algotithim. 
    
    Given N0 and N1 as the input numbers, each of length n (a power of two):
    
    1) pad N0 and N1 with n zeros in the high-order positions (why do we do this?)
    2) evaluate N0 and N1 at 2n primitive roots of unity (use the forward FFT),
        S0 <-- FFT(N0+pad),  S1 <-- FFT(N0+pad)
    3) element-wise multiply the output of the evaluations of N0 and N1,  
        S <-- S0[i]*S1[i], 0<=i < 2*n
    4) interpolate using the inverse FFT
    5) extract the real coefficients and round each to integers
    '''   
    #1
    for i in range(0, len(N0)):
        N0.append(0)
        N1.append(0)

    #2
    n = len(N0)
    S0 = fft([complex(N0[i],0) for i in range(0,n)], getV(n, 1), n)
    S1 = fft([complex(N1[i],0) for i in range(0,n)], getV(n, 1), n)
    
    #3
    S = [(S0[i]*S1[i]) for i in range(0, n)]
    
    #4
    Sinv = fft(S, getV(n, -1), n)
    
    #5
    final = [int(((Sinv[i].real)/n)) for i in range(0, n)]   
    return final

def getV(n, sign = 1):
    return [complex(cos(2*pi*i/n), sign * sin(2*pi*i/n)) for i in range(0, n)]

def bit_reverse_traverse_no_generator(a):
    n = a.shape[0]
    assert(not n&(n-1))
    if n == 1:
        return a
    else:
        even_indicies = np.arange(n//2)*2
        odd_indicies = np.arange(n//2)*2 + 1
        evens = bit_reverse_traverse_no_generator(a[even_indicies])
        odds = bit_reverse_traverse_no_generator(a[odd_indicies])
        return np.concatenate([evens, odds])

def get_bit(l):
    n = len(l)
    indexs = np.arange(n)
    b = []
    for i in bit_reverse_traverse_no_generator(indexs):
        b.append(l[i])
    return b

def fft(p, v, n, depth = 0):
    #print("%s%s" % (" |"*depth+"in =", str(p)))
    if n == 1:
        #print("%s%s" % (" |"*depth+"out=", str(p)))
        return p 
    # split into even and odd
    eve = [p[i] for i in range(0, n, 2)]
    odd = [p[i] for i in range(1, n, 2)]
    # square the v values
    v2 = [v[i]*v[i] for i in range(0, n//2)]
    # solve the two sub problems
    eveS = fft(eve, v2, n//2, depth+3)
    oddS = fft(odd, v2, n//2, depth+3)
    # construct the solution
    solution = ([eveS[i] + v[i]*oddS[i] for i in range(0, n//2)] + 
                [eveS[i] - v[i]*oddS[i] for i in range(0, n//2)])
    #print("%s%s" % (" |"*depth+"out=", str(solution)))
    return solution
    
def DPfft(p,v,n,depth=0):
    #set up cache
    C = np.array([[0 for j in range(0, n)] for i in range(0,int(math.log(n,2))+1)], dtype=complex)

    #base cases, reverse bit sort
    rev = get_bit([i for i in range(0,n)])
    for i in range(0, n):
        C[0,i] = p[int(rev[i].real)]
    
    #fill in the cache
    for i in range(1, int(log(n,2))+1):
        size = 2**i
        for j in range(0, n, size):
            for k in range(0, size//2):
                #index into v should be a combination of i, j, and k
                tmp = ((j//n)*(k)//(i))
                C[i,j+k]         = C[i-1,j+k] + v[tmp] * C[i-1,j+size//2+k]
                C[i,j+size//2+k] = C[i-1,j+k] - v[tmp] * C[i-1,j+size//2+k]
    
    #return the solution
    return C[int(math.log(n,2))]

def run():
    #used to make sure that fft and dpfft get the same results. 
    # n = 8
    # p = [0, 1, 2, 3, 4, 5, 6, 7]
    # #p = [0, 1, 2, 3] 
    # print("Forward FFT")
    # sol=fft([complex(p[i],0) for i in range(0,n)], getV(n, 1), n)
    # print(sol)
    # print("Inverse FFT")
    # back=fft(sol, getV(n, -1), n)
    # for i in range(0, len(back)):
    #     back[i] = back[i]/n
    # print(back)
    # print()
 
    # print("Forward DP FFT")
    # sol=DPfft([complex(p[i],0) for i in range(0,n)], getV(n, 1), n)
    # print(sol)
    # print("Inverse DP FFT")
    # back=DPfft(sol, getV(n, -1), n)
    # for i in range(0, len(back)):
    #     back[i] = back[i]/n
    # print(back)
    # print()
    
    #Graph the runtimes of the two algos. 
    number = []
    FFTresults = []
    DPfftresults = []
    i = 128
    #67108864
    while(i <= 1048576):
        print("Running simulation: "+str(i))
        number.append(i)
        p = [random.randint(0, i) for x in range(0, i)]
        start = time.time()
        fft([complex(p[n],0) for n in range(0,i)], getV(i, 1), i)
        total = time.time() - start
        FFTresults.append(total)
        start = time.time()
        DPfft([complex(p[n],0) for n in range(0,i)], getV(i, 1), i)
        total = time.time() - start
        DPfftresults.append(total)        
        i = 2*i
    
    plt.plot(FFTresults, number, 'r', label='FFT')
    plt.plot(DPfftresults, number, 'b', label='DP FFT')
    plt.xlabel("Run time, seconds")
    plt.ylabel("Number of elements")
    plt.title("FFT vs DP FFT")
    plt.yscale('log')
    plt.xscale('log')
    plt.legend()
    plt.show()
    