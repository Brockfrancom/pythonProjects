"""
Brock Francom
A02052161
CS-1400-001
Douglas Galarus
2/15/2018
hw6 - Exercise 5.34
"""
   
def run():
    #import random and assign variables
    import random
    lotteryDigit1 = 0
    lotteryDigit2 = 0
    
    #loop is used to generate 2 different digits
    while lotteryDigit1 == lotteryDigit2:    
        lottery = random.randint(00, 99)
        lotteryDigit1 = lottery // 10
        lotteryDigit2 = lottery % 10
        
    #user input
    user = int(input("Enter a number (2 digits): "))
    
    #evaluate user input
    userDigit1 = user // 10
    userDigit2 = user % 10
    
    #print results
    if user == lottery:
        print("Exact match! You win $10,000!")
    elif userDigit1 == lotteryDigit2 and userDigit2 == lotteryDigit1:
        print("Matched all digits! You win $3,000!")
    elif userDigit1 == lotteryDigit1 or userDigit1 == lotteryDigit2 \
            or userDigit2 == lotteryDigit1 or userDigit2 == lotteryDigit2:
        print("Matched 1 digit. You win $1,000!")
    else:
        print("Sorry no match.")

















