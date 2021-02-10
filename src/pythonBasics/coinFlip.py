"""
Brock Francom
A02052161
CS-1400-001
Douglas Galarus
2/15/2018
hw6 - Exercise 5.40
"""

#import random and reset counts to 0
import random
def run():
    heads = 0 
    tails = 0
    count = 0
    
    #flip a coin 1000000 times and record results
    while count < 1000000:
        flip = random.randint(0,1)
        if flip == 0:
            heads += 1
        else:
            tails += 1
        count += 1
    
    #print results  
    print("Heads: ", heads)
    print("Tails: ", tails)










