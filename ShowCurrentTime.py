"""
Brock Francom
A02052161
CS-1400-001
Douglas Galarus
1/24/2018
hw3 - 3-2-18

2.18 (Current time) Listing 2.7, ShowCurrentTime.py, gives a program that displays 
the current time in GMT. Revise the program so that it prompts the user to enter 
the time zone in hours away from (offset to) GMT and displays the time in the 
specified time zone. Here is a sample run:

Enter the time zone offset to GMT: -5

The current time is 4:50:34

"""
#get timezone offset
offset = eval(input("Enter the time zone offset to GMT: "))
#formating
print("\n")

import time

currentTime = time.time() #get current time

#format time
totalSeconds = int(currentTime)
currentSecond = totalSeconds % 60
totalMinutes = totalSeconds // 60
currentMinute = totalMinutes % 60
totalHours = totalMinutes // 60
currentHour = (((totalHours % 24) - offset) % 12) #calculate hour with timezone offset


#print time
print("The current time is " + str(currentHour) + ":" + str(currentMinute) + ":" + str(currentSecond))














