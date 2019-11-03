"""
Brock Francom
A02052161
CS-1440
Erik Falor
10/17/2018
3: Bingo Cards
"""
import random

class NumberSet():
    def __init__(self, size):
        """NumberSet constructor"""
        self.__size = size
        self.__numberSet = []
        i = 1
        while i <= size:
            self.__numberSet.append(i)
            i += 1
        
    def getSize(self):
        """Return an integer: the size of the NumberSet"""
        return self.__size

    def get(self, index):
        """Return an integer: get the number from this NumberSet at an index"""
        return self.__numberSet[index]


    def randomize(self):
        """void function: Shuffle this NumberSet"""
        random.shuffle(self.__numberSet)

    def getNext(self):
        """Return an integer: when called repeatedly return successive values
        from the NumberSet until the end is reached, at which time 'None' is returned"""
        return self.__numberSet.pop()
        