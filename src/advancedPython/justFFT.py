'''
Brock Francom
A02052161
Assignment 9 
'''
import numpy as np
import random
import time
import matplotlib.pyplot as plt
from math import *

def highSchoolMult(P, Q, n, m):
    PQ = np.zeros((2*n))
    for i in range(0,n):
        for j in range(0,m):
            PQ[i+j] += P[i]* Q[j]
    return PQ

def DCmult3Sub(P, Q, n, m):
    PQ = np.zeros((2*n))
    if n==1:
        PQ[0] = P[0]*Q[0]
        return PQ
        
    Qlh = np.zeros((m//2))
    Plh = np.zeros((n//2))
    for i in range(0, (n//2)):
        Plh[i] = P[i] + P[i+(n//2)]
    for i in range(0, m//2):
        Qlh[i] = Q[i] + Q[i+(m//2)]
        
    PQLL = DCmult3Sub(P[0:n//2], Q[0:m//2], n//2, m//2)
    PQHH = DCmult3Sub(P[n//2:], Q[m//2:], n//2, m//2)
    So = DCmult3Sub(Plh, Qlh, n//2, m//2)
    So = So - PQLL - PQHH
    
    for i in range(0,n):
        PQ[i] += PQLL[i]
        PQ[i+(n//2)] += So[i]
        PQ[i+n] += PQHH[i]
    return PQ

def getV(n, sign = 1):
    return [complex(cos(2*pi*i/n), sign * sin(2*pi*i/n)) for i in range(0, n)]

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

def run():
    #1 and 2
    # This section compares answers returned by the HS and FFT algorithims. 
    # This section also calculates the inaccuracy between solutions. 
    i = 4
    while(i <= 128):
        print("Running simulation: {}".format(i))
        N0 = [random.randint(0, 1000) for m in range(0, i)]
        N1 = [random.randint(0, 1000) for m in range(0, i)]

        sol1 = highSchoolMult(N0, N1, len(N0), len(N1))
        sol2 = polyMultFFT(N0, N1)
        
        print("Checking solution for simulation {}".format(i))
        totalErr = 0 
        for j in range(0, i):
            assert abs(int(sol1[i]) - sol2[i]) <= 1
            totalErr += abs(int(sol1[i]) - sol2[i])
        print("solution matches for simulation {}".format(i))
        totalErr = totalErr/(2*i)
        print("Total error: {}".format(totalErr))
        print()
        i = 2*i
        
    #3 This is where we make comparisons between the three algorithims. 
    #  Each will run for around 20 minutes CPU time and we will see how big 
    #  of a problem size they can get to. 
    number = []
    HSresults = []
    DC3SubResults = []
    FFTresults = []
    # Booleans that tell us if we should run the algorithim or not. 
    runHS = True
    runDC3Sub = True
    runFFT = True
    i = 4
    while(True):
        number.append(i)
        A = [random.randint(0, i) for x in range(0, i)]
        B = [random.randint(0, i) for x in range(0, i)]
        if runHS:
            print("Running HS simulation: {}".format(i))
            start = time.time()
            C = highSchoolMult(A, B, len(A), len(B))
            total = time.time() - start
            if total > 1200:
                runHS = False
            HSresults.append(total)
        else:
            HSresults.append(0)
        if runDC3Sub:
            print("Running DC3Sub simulation: {}".format(i))
            start1 = time.time()
            C = DCmult3Sub(A, B, len(A), len(B))
            total1 = time.time() - start1
            if total1 > 1200:
                runDC3Sub = False
            DC3SubResults.append(total1)
        else:
            DC3SubResults.append(0)
        if runFFT:
            print("Running FFT simulation: {}".format(i))
            start2 = time.time()
            C = polyMultFFT(A, B)
            total2 = time.time() - start2
            if total2 > 1200:
                runFFT = False
            FFTresults.append(total2)
        if not runHS and not runDC3Sub and not runFFT:
            break
        i = 2*i    
    
    #Plot the results
    plt.plot(number, HSresults, 'b', label='HS')
    plt.plot(number, DC3SubResults, 'g', label='3 Sub')
    plt.plot(number, FFTresults, 'g', label='FFT')
    plt.yscale('log')
    plt.xscale('log')
    plt.ylabel("Run time, seconds")
    plt.xlabel("Number of elements")
    plt.title("Polynomial multipy, HS vs 3 Sub vs FFT")
    plt.legend()
    plt.show()
    plt.savefig('graph3algorithims.png')
    
    #Save the data
    with open("Timing.txt", 'w+') as f:
        f.write("HS results\n")
        f.write(str(HSresults))
        f.write('\nDC3Sub results\n')
        f.write(str(DC3SubResults))
        f.write('\nFFT results\n')
        f.write(str(FFTresults))
 