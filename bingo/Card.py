"""
Brock Francom
A02052161
CS-1440
Erik Falor
10/17/2018
3: Bingo Cards
"""
import sys

import NumberSet

class Card():
    def __init__(self, idnum, size, numberSet):
        self.__idnum = idnum
        self.__size = size
        self.__numberSet = numberSet
        self.__numberSet2 = numberSet
        
        
    def getId(self):
        """Return an integer: the ID number of the card"""
        return self.__idnum

    def getSize(self):
        """Return an integer: the size of one dimension of the card.
        A 3x3 card will return 3, a 5x5 card will return 5, etc.
        """
        return self.__size

    def print(self, file=sys.stdout):
        """void function:
        Prints a card to the screen or to an open file object
        There is a lot of formatting going on in this function
        """
        print(f"Card #{self.getId()}:", file=file)
        i = 0
        d = 0
        while i < self.__size:
            m = 0
            print("+-----+"*int(self.__size), file=file)
            while m < int(self.__size):
                j = str(self.__numberSet2[d])
                print("|", end="", file=file)
                print(j.center(5), end="", file=file)
                print("|", end="", file=file)
                m += 1
                d += 1
            print(file=file)
            i += 1
        print("+-----+"*int(self.__size), file=file)
        self.__numberSet2 = self.__numberSet
            