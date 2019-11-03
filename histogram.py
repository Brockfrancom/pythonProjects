"""
Brock Francom
A02052161
CS-1400-001
Douglas Galarus
4/3/2018
hw11 - Exercise 10.19

Note: In order for the histogram to be displayed nicely, you must choose a 
number of slots such that all can be seen in one line of the command prompt. 
Otherwise the formating gets messed up. On my laptop, slot numbers ranging 
from 1 to 50 seem to work fine on my laptop, if the command prompt window 
is maximized. 

Also I added a scale to the histogram to make it easier to read.

Thanks!
"""
#get user input and create an empty list of balls
import random
balls = eval(input("Enter the number of balls to drop: "))
slots = eval(input("Enter the number of slots in the bean machine: "))
lst = list(range(balls))
#create an empty list to count the slot it falls into, and then for each ball 
#randomly generate a direction to fall and record
countlst = []
for i in lst:
    slots1 = slots - 1
    lst[i] = ''
    count = 0
    while slots1 > 0:
        rand = random.randint(0,1)
        if rand == 0:
            lst[i] += 'L'
        else:
            lst[i] += 'R'
            count += 1
        slots1 -= 1
    countlst.append(count)
#formating
print('')
#print ball paths
for i in lst:
    print(i)
#formating
print('')
#make a list of how many balls are in each slot
number = 0
counts = []
while number < slots:   
    counts.append(countlst.count(number))
    number += 1
#get slot totals and display a histogram, if a slot is empty, the slot it blank.
#make the command window large if using large amounts of slots, so all slots are
#displayed on one line. This makes the graph easier to read.   
m = max(counts)
for i in range(m, -1, -1):
    for j in counts:
       print("0" 
             if j > 0 and i < j
             else " ",
             end = "  ")
    print()

#print a scale, this wasn't specified, but it makes the histogram easier to read.
for i in range(0, slots):
    i = i + 1
    print((str(i) + ' ') if i < 10 else i, end = " ")
    
    
    
    
    
    