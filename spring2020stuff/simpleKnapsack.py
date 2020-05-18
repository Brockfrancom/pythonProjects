#Brock Francom
#A02052161
'''
In this assignment you will:

1)  test the attached simple knapsack code with some simple examples and 
    convince your self it works. Add comments to each conditional 
    statement. Note how in this code the list of objects begins with 
    None. This is because the variable "i" in the function refers to 
    the number of objects, not the index into the array. That is why 
    we can terminate on i==0 meaning no objects. Don't change this scheme.

2)  Expand the knapsack function to solve a different and more complex 
    problem. In this new problem:

    There are two independent knapsacks, of size K1 and K2 (ints). An object
    may be thrown away, put in the first knapsack or put in the second knapsack.

    The function is no longer a Bool in this simple code which is solving a 
    decision problem. Rather the new function returns a float because it is 
    solving an optimization problem. In this problem, each object has a size 
    and a value. So the problem is described by two arrays of size N+1. S 
    containing integers >= 1. And V containing positive floats. 

    The function should return the maximum value that can be obtained by 
    picking a subset of objects from S. The subset of objects must fit into 
    the knapsacks. So the sum of the objects picked from knapsack 1 must be 
    less than or equal to K1, likewise for knapsack 2. The sum of the values 
    for those objects must be the maximum obtainable (over all possible 
    subsets of objects).

    Before you panic thinking about how to write this code. Take a breath
    and apply the meta-algorithm to the problem. If you do that, you should
    arrive at a fairly simple function that requires about 8 lines of code. 
    Test the code with some very simple examples. Note, this code does not
    have to determine the actual objects that are best.

3)  Write a simple problem generator that takes N and aveSize and returns
    two arrays S and V containing N+1 entries, where the size of the 
    objects is random and in the range from 1 to 2*aveSize. The values 
    can be any positive float.

4)  Write the Memoizing function by copying the recursive code and modifying
    it

5)  Write the DP code by copying the recursive code and modifying it.

6)  Perform the following experiment: for 10 different aveSize values, 
    determine the execution time of the DP and the memoizing function 
    (with fixed K1 and K2 and N, make them big enough so the code run
    time can be measured). For each aveSize, measure the time over 20 
    independent runs. Plot a graph of aveSize (independent variable) vs. 
    run time (dependent variable). The graph should have two lines on it,
    one for DP and one for memoizing.
'''
###########################
from random import random, randint
import time
import matplotlib.pyplot as plt


def knapsackBool(i, size):
    # If the knapsack is full without space left over, return true.
    if size == 0:
        return True
    # If the knapsack is overful, then the problem is false. 
    if size < 0:
        return False
    # If there are no other items, return False. 
    if i == 0:
        return False
    return knapsackBool(i-1, size) or knapsackBool(i-1, size - S[i])

def twoKnapsackFloat(i, k1, k2):
    if i == len(V):
        return 0
    one, two, three = 0,0,0
    #Put in K1
    if (S[i]) <= k1:
        one =  V[i] + twoKnapsackFloat(i+1, k1-S[i], k2)
    #Put in K2
    if (S[i]) <= k2:
        two = V[i] + twoKnapsackFloat(i+1, k1, k2-S[i])
    #Throw away
    three = twoKnapsackFloat(i+1, k1, k2)
    return max(one, two, three)

        

def twoKnapsackMemoized(k1, k2):
    for c in range(len(S)):
        one, two, three = 0,0,0
        for a in range(k1+1):
            for b in range(k2+1):
                #Put in K1
                if (S[c]) <= a:
                    one = max(V[c] + memoizedCache[a-1][b], memoizedCache[a][b-1]) #twoKnapsackFloat(i+1, k1-S[i], k2)
                #Put in K2
                if (S[c]) <= b:
                    two = max(V[c] + memoizedCache[a][b-1], memoizedCache[a-1][b]) #twoKnapsackFloat(i+1, k1, k2-S[i])
                #Throw away
                three = max(memoizedCache[a][b-1], memoizedCache[a-1][b]) #twoKnapsackFloat(i+1, k1, k2)
                memoizedCache[a][b] = max(one, two, three)
    return memoizedCache[k1][k2]

def twoKnapsackDP(k1, k2):
    for i in range(1,len(S)):
        for w1 in range(k2, S[i], -1):
            for w2 in range(k1, S[i], -1):
                dpCache[w2][w1] = max(dpCache[w1][w2],
                       (dpCache[(w1 - S[i])][w2] + V[i]),
                       (dpCache[w1][(w2 - S[i])] + V[i]))   
    return dpCache[k2][k1]
    
def generateProblem(N, aveSize):
    S = []
    V = []
    for i in range(0, N+1):
        S.append(randint(1, (2*aveSize)))   
        V.append(random()*10)
    return S, V

if __name__ == "__main__":
    '''    
    for _ in range(0,100):
        S = [randint(1,K/2) for _ in range(0,N + 1)]
        if knapsackBool(N, K):
            print("Solution exists")
        else:
            print("Solution does not exist")
    '''        
    '''   
    N = 1
    K = 20
    S = [None, 10,10]
    print(knapsackBool(N, K))
    '''
    '''
    S = [4, 5, 5, 6]
    V = [1.2, 3.4, 10.0, 300]
    K1 = 10
    K2 = 5    
    print(twoKnapsackFloat(0, K1, K2))
    
    S = [4, 5, 5, 6]
    V = [1.2, 3.4, 10.0, 300]
    K1 = 10
    K2 = 5
    memoizedCache = []
    for i in range(K1+1):
        row = []
        for j in range(K2+1):
            row.append(0)
        memoizedCache.append(row)

    
    #print(twoKnapsackMemoized(K1, K2))
    dpCache = [[0 for i in range(K1+1)] for j in range(K2+1)]
    print(twoKnapsackDP(K1, K2))
    
    '''
    """
    Perform the following experiment: for 10 different aveSize values, 
    determine the execution time of the DP and the memoizing function 
    (with fixed K1 and K2 and N, make them big enough so the code run
    time can be measured). For each aveSize, measure the time over 20 
    independent runs. Plot a graph of aveSize (independent variable) vs. 
    run time (dependent variable). The graph should have two lines on it,
    one for DP and one for memoizing.
    """

    #If my memoized and dp funcitons worked, this would be the code for the tests.
    K1 = 10
    K2 = 10
    N = 5
    avgSize = [5, 34, 50, 53, 100, 150, 250, 350, 500, 2000]
    memoizedResults = []
    dpResults = []
        
    for i in avgSize:
        temp = []
        for j in range(0, 20):
            S, V = generateProblem(N, i)
            memoizedCache = [[0 for i in range(K1+1)] for j in range(K2+1)]
            start = time.time()
            twoKnapsackMemoized(K1, K2)
            total = time.time() - start
            temp.append(total)
        memoizedResults.append(temp)
         
    for i in avgSize:
        temp = []
        for j in range(0, 20):
            S, V = generateProblem(N, i)
            dpCache = [[0 for i in range(K2+1)] for j in range(K1+1)]
            start = time.time()
            twoKnapsackDP(K1, K2)
            total = time.time() - start
            temp.append(total)
        dpResults.append(temp)
    
    finalAvgMem = []
    finalAvgDp = []
    for i in range(0, 10):
        mem = 0
        dp = 0
        for j in range(0, 20):
            mem += memoizedResults[i][j]
            dp += dpResults[i][j]
        finalAvgMem.append(mem/20)
        finalAvgDp.append(dp/20)
        
    plt.plot(avgSize, finalAvgMem, 'b', label='Memoized')
    plt.plot(avgSize, finalAvgDp, 'r', label='Dynamic')
    plt.ylabel("Run time, seconds")
    plt.xlabel("Average size")
    plt.title("Runtimes for memoized and dynamically programmed knapsack")
    plt.legend()
    plt.show()
