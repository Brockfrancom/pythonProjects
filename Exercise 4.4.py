"""
Brock Francom
A02052161
CS-1400-001
Douglas Galarus
2/8/2018
hw Exercise 4.4
"""
#generate random integers
import random
number1 = random.randint(0,99)
number2 = random.randint(0,99)

#prompt user
print(number1, "+", number2, "=")

#user input
answer1 = eval(input("Answer: "))

#print true or false
if answer1 == (number1 + number2):
    print("True")
else:
    print("False")
    