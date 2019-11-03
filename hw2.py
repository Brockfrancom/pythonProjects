"""
Brock Francom
A02052161
CS-1400-001
Douglas Galarus
1/17/2018
hw2 - Calculate your score

NOTE:: This code will seperate the inputs with an extra line. I talked to the 
professor and he said that this would be ok, because to fix that it would take 
more advanced programming.

"""

#ask user for scores
homework = eval(input("Please enter how many homework points you earned, out of 150: "))
exam = eval(input("Please enter how many exam points you earned, out of 250: "))
recitation = eval(input("Please enter how many recitation points you earned, out of 75: "))

#calculate total points
TOTALPOINTS = 475
total = homework + exam + recitation
print("Total points out of 475:", total)

#calculate percentage
percent = total/TOTALPOINTS
print("Final percentage:", format(percent, "4f"))

#print message
if percent >= .94:
    print("You got an A! You are a big deal!")
    
    
    
    
    
    
    
    