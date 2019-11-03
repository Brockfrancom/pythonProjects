"""
Brock Francom
A02052161
CS-1400-001
Douglas Galarus
3/1/2018
hw8 - Exercise 6.28
"""
import random

#function for rolling the dice
def rollDice():
    roll = random.randint(1,6)
    return roll

#function to execute if not won on the first run
def rollDice2():
    while True:
        a = rollDice()
        b = rollDice()
        k = a + b
        print("You rolled " + str(a) + " + " + str(b) + " = " + str(k))
        if k == m:
            return "You win"
        elif k == 7:
            return "You lose"
        else:
            return rollDice2() #if not a win re-run the function
        
#main program, first roll and if it matches, print win/loss, else enter second function
a = rollDice()
b = rollDice()
m = a + b
print("You rolled " + str(a) + " + " + str(b) + " = " + str(m))
if m == 2 or m == 3 or m == 12:
    print("You lose")
elif m == 7 or m == 11:
    print("You win")
else:
    print("point is " + str(m))
    print(rollDice2())      
    

















