"""
Brock Francom
A02052161
NIM game
"""
import time
import matplotlib.pyplot as plt

def run():
    beginning = time.time()
    #Global variables for Mimorized solution
    N = 3000 #Set super high so that if you want to run just the Mimorized 
             #solution, you will have enough space in your arrays. Max is 2956.
    done = [False] * N
    W = [False] * N
    mimoizedResults = [False] * N
    
    #Global variables for recursive solution
    # 55 takes approx 5 minutes total.
    
    numberOfStones = 40
    timing = [False] * numberOfStones
    num = list(range(numberOfStones))
    results = [False] * numberOfStones
    
    #Recursive solution
    def oldWin(n):
        if n==0:
            return True
        if n==1:
            return False
        return not(oldWin(n-1) and oldWin(n-2))        
    
    #Mimoized solution
    def win(n):
        if n==0:
            W[n] = True
            done[n] = True
            return W[n]
        if n==1:
            W[n] = False
            done[n] = True
            return W[n]
        if done[n]:
            return W[n]
        W[n] = not(win(n-1) and win(n-2))
        done[n] = True
        return W[n]
    
    #Run the recursive solution, time each iteration. 
    for i in range(0, numberOfStones):
        print("Running recursive simulation size {}.".format(i))
        start = time.time()
        results[i] = oldWin(i)
        timing[i] = time.time() - start
    
    #Print results    
    print("\nRecursive solution Results:")
    for i in range(0, numberOfStones):
        print("n = {}; time = {} seconds.".format(i,timing[i]))
        
    #Plot the results on a logarithmic scale graph. 
    plt.plot(num,timing)
    plt.yscale('log')
    plt.ylabel("Run time")
    plt.xlabel("n - number of stones")
    plt.title("NIM recusive")
    plt.show()
    
    #Calculate slope of the line.
    total = 0
    for i in range(0, numberOfStones):
        total += timing[i]
    print("The slope of the line is approxamatly {}.".format((total/(numberOfStones))))
    
    #Run the mimoized solution  
    for i in range(0, numberOfStones):
        mimoizedResults[i] = win(i)
    
    #Make sure all answers are the same for both solutions.
    allCorrect = True
    for i in range(0, numberOfStones):
        if mimoizedResults[i] != results[i]:
            allCorrect = False
            print("Values for {} do not match, Recursive = {}; Mimozied = {};".format(i, results[i], W[i]))
    if allCorrect:
        print("\nAll values matched.")
    print("Simulation took a total of {} minutes.".format((time.time() - beginning)/60))
    
    #print(win(2956))