'''
Brock Francom
A02052161
Assignment 5 
'''
import numpy as np
import random
import time
import matplotlib.pyplot as plt

def highSchoolMult(P, Q, n, m):
    PQ = np.zeros((2*n))
    for i in range(0,n):
        for j in range(0,m):
            PQ[i+j] += P[i]* Q[j]
    return PQ

def DCmult(P, Q, n, m):
    PQ = np.zeros((2*n))
    if n==1:
        PQ[0] = P[0]*Q[0]
        return PQ
    PQLL = DCmult(P[0:n//2], Q[0:m//2], n//2, m//2)
    PQLH = DCmult(P[0:n//2], Q[m//2:], n//2, m//2)
    PQHL = DCmult(P[n//2:], Q[0:m//2], n//2, m//2)
    PQHH = DCmult(P[n//2:], Q[m//2:], n//2, m//2)  
    for i in range(0,n):
        PQ[i] += PQLL[i]
        PQ[i+n//2] += PQLH[i]
        PQ[i+n//2] += PQHL[i]
        PQ[i+n] += PQHH[i]
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

######################### Comparison of algorithims ##################

number = []
HSresults = []
DCresults = []
DC3SubResults = []
i = 4
while(i <= 32768):
    number.append(i)
    A = [random.randint(0, i) for x in range(0, i)]
    B = [random.randint(0, i) for x in range(0, i)]
    start = time.time()
    C = highSchoolMult(A, B, len(A), len(B))
    total = time.time() - start
    HSresults.append(total)
    start2 = time.time()
    C = DCmult(A, B, len(A), len(B))
    total2 = time.time() - start2
    DCresults.append(total2)
    start3 = time.time()
    C = DCmult3Sub(A, B, len(A), len(B))
    total3 = time.time() - start3
    DC3SubResults.append(total3)
    i = 2*i

hsSlope, intercept = np.polyfit(np.log(number), np.log(HSresults), 1)
DCs, intercept = np.polyfit(np.log(number), np.log(DCresults), 1)
DC3s, intercept = np.polyfit(np.log(number), np.log(DC3SubResults), 1)

plt.plot(number, HSresults, 'b', label='HS, Slope: '+str(hsSlope)[:6])
plt.plot(number, DCresults, 'r', label='Divide, Slope: '+str(DCs)[:6])
plt.plot(number, DC3SubResults, 'g', label='3 Sub, Slope: '+str(DC3s)[:6])
plt.yscale('log')
plt.xscale('log')
plt.ylabel("Run time, seconds")
plt.xlabel("Number of elements")
plt.title("Polynomial multipy, HS vs DC vs 3 Sub")
plt.legend()
plt.show()
plt.savefig('graph3algorithims.png')

with open("output.txt", 'w+') as f:
    f.write(HSresults)
    f.write('\n')
    f.write(DCresults)
    f.write('\n')
    f.write(DC3SubResults)
