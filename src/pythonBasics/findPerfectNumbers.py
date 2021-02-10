"""
Brock Francom
A02052161
CS-1400-001
Douglas Galarus
2/15/2018
hw6 - Exercise 5.35
"""

def run():
    #set counts
    perfect = 0
    number = 2
    divisor = 1
    
    print("The perfect numbers are:")
    #check all the numbers to 10000
    while number < 10000:
        while divisor <= (number / 2): #does it factor?
            if (number % divisor) == 0:
                perfect += divisor  #it factors, record the factor
                #is it a perfect number and have we checked all the factors?
                if perfect == number and divisor == (number / 2): 
                    print(perfect)
                    perfect = 0 #reset counts
                    divisor = 1
                    break
                else:
                    divisor += 1 
            else:
                divisor += 1
        perfect = 0
        divisor = 1
        number += 1 #reset counts and check the next number






