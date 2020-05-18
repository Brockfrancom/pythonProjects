# Min hemming distance algorithm
# HW4

import numpy as np
import time
import random

def MED(A, B, i, j):
    if i==0: #first string is empty, return second string
        return j
    if j==0: #second string is empty, return first string 
        return i
    if i<0 or j<0:
        return 99999999999
    return min(MED(A, B, i-1, j)+1, MED(A, B, i, j-1)+1, (MED(A, B, i-1, j-1)+(A[i-1]!=B[j-1])))

def dpMED(A, B, m, n): 
    #C2 = [[0 for x in range(0, n+1)] for y in range(0, m+1)]    
    C2 = np.zeros([n+1,m+1])
    for i in range(0, m+1): 
        for j in range(0, n+1):   
            #first string is empty, insert second string 
            if i == 0: 
                C2[i][j] = j  
            #second string is empty, insert first string 
            elif j == 0: 
                C2[i][j] = i 
            #characters are same, ignore them and continue
            elif A[i-1] == B[j-1]:
                C2[i][j] = C2[i-1][j-1]   
            #characters are different, find minimum 
            else: 
                C2[i][j] = 1 + min(C2[i][j-1], C2[i-1][j], C2[i-1][j-1])   
    return (C2[m][n]), C2 

dnaScoring = {'aa':5, 
              'ac':-1, 
              'ag':-2, 
              'at':-1, 
              'a_':-3, 
              'cc':5, 
              'cg':-3, 
              'ct':-2, 
              'c_':-4, 
              'gg':5, 
              'gt':-2, 
              'g_':-2, 
              'tt':5, 
              't_':-1,
              'ca':-1, 
              'ga':-2, 
              'ta':-1, 
              '_a':-3, 
              'gc':-3, 
              'tc':-2, 
              'tg':-2,
              '_c':-4, 
              '_g':-2, 
              '_t':-1}

def dpMEDdna(A, B, n, m):
    C2 = np.zeros([n+1,m+1])
    for i in range(1, n+1):
        C2[i, 0] = C2[i-1, 0] +dnaScoring[A[i-1]+'_']

    for i in range(1, m+1):
        C2[0, i] = C2[0, i-1] + dnaScoring['_'+B[i-1]]
    for i in range(1, n+1): 
        for j in range(1, m+1):
            C2[i, j] =  max(C2[i, j-1] + dnaScoring['_'+B[j-1]], 
                            C2[i-1, j] + dnaScoring[A[i-1]+'_'],
                            C2[i-1, j-1] + dnaScoring[A[i-1]+B[j-1]])
    return (C2[n][m]), C2
 
def backtrace(C, A, B, i, j):
    while(True):
        if i == 0 and j == 0:
            break
        nextVal = max(C[i,j-1], C[i-1,j], C[i-1,j-1])
          
        if C[i-1,j-1] == nextVal:
            if A[i-1] == B[j-1]:
                SC.append((A[i-1], '=', B[j-1]))
            else:
                SC.append((A[i-1], '->', B[j-1]))
            return backtrace(C, A, B, i-1, j-1)
    
        if i < j:
            SC.append(('_', '->', B[j-1]))
            return backtrace(C, A, B, i, j-1)
        if j < i:
            SC.append((A[i-1], '->', '_'))
            return backtrace(C, A, B, i-1, j)
        
        if C[i-1, j] == nextVal:
            SC.append(('_', '->', B[j-1]))
            return backtrace(C, A, B, i-1, j)
        
        elif C[i, j-1] == nextVal:
            SC.append((A[i-1], '->', '_'))
            return backtrace(C, A, B, i, j-1)
        else:
            pass
    for k in range(len(SC)-1, -1, -1):
        print(SC[k])
    
################################## Testing ###################################
'''
Do some simple experiments to estimate the speed of the algorithm as a 
function of the length of the DNA sequence. Here generate random 
sequences of ACGTs of increasing lengths. What size of the solution 
matrix does the algorithm become impractical? 
'''
###################Testing for the algorithim. ###########################

#the random int from 0-3 correspond are equivalent to A:0, C:1, G:2, T:3
'''
timing = []
for i in range(1000, 6000, 1000):
    A = [random.randint(0, 4) for j in range(i)]
    B = [random.randint(0, 4) for j in range(i)]
    start = time.time()
    res, cache = dpMED(A,B,len(A),len(B))
    total = time.time() - start
    timing.append((i, total))
'''    
'''
In conclusion of the testing, I found that the algorithim complexity was 
approxamatly O(n^2). (See screenshot for timing results.)
'''    
     
'''
print("\nShould be 2:")
A='aaagct'
B='cgtacg'  
res, cache = dpMEDdna(A,B,len(A),len(B))
print(res)
SC = []
backtrace(cache, A, B, len(A), len(B))
#printBacktrace(A, B, SC, 0, 0)

print("\nShould be -2:")
A='aaagcttttt'
B='cgtacg'  
res, cache = dpMEDdna(A,B,len(A),len(B))
print(res)
SC = []
backtrace(cache, A, B, len(A), len(B))
#printBacktrace(A, B, SC, 0, 0)

print("\nShould be 17:")
A='aaaa'
B='aaaaa'  
res, cache = dpMEDdna(A,B,len(A),len(B))
print(res)
SC = []
backtrace(cache, A, B, len(A), len(B))
#printBacktrace(A, B, SC, 0, 0)

print("\nShould be 18:")
A='aaaaa'
B='aaaag'  
res, cache = dpMEDdna(A,B,len(A),len(B))
print(res)
SC = []
backtrace(cache, A, B, len(A), len(B))
#printBacktrace(A, B, SC, 0, 0)
   
print("\nShould be 10:")
A='acgtacgt'
B='acgt'  
res, cache = dpMEDdna(A,B,len(A),len(B))
print(res)
SC = []
backtrace(cache, A, B, len(A), len(B))
#printBacktrace(A, B, SC, 0, 0)

print("\nShould be 24:")
A='aaaaacg'
B='gaaaaag'  
res, cache = dpMEDdna(A,B,len(A),len(B))
print(res)
SC = []
backtrace(cache, A, B, len(A), len(B))
#printBacktrace(A, B, SC, 0, 0)
'''