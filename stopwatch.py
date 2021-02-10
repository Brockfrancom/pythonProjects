"""
Brock Francom
A02052161
CS-1400-001
Douglas Galarus
3/14/2018
hw9 - Exercise 7.8
"""
import time

#create class
class Stopwatch:
    def __init__(self):#create data feilds
        self.__startTime = time.time()
        self.__endTime = 0.0
        
    def start(self):#create method to modify __startTime
        self.__startTime = time.time()
    def stop(self):#create method to modify __endTime
        self.__endTime = time.time()
    def getElapsedTime(self):#calculate elapsed time and return in m
        m = (self.__endTime - self.__startTime)
        return m
    def getStartTime(self):
        return self.__startTime
#program to test stopwatch

def run():
    #create object stopwatch
    num = Stopwatch()
    i = 1
    #start stopwatch
    num.start()
    #count to 1000000
    while i < 1000000:
        i = i + 1
    #stop stopwatch
    num.stop()
    #display elapsed time in miliseconds, format time as well, the book didn't 
    #specify this but I did.
    print(format((num.getElapsedTime() * 100), '2.4f'))


























