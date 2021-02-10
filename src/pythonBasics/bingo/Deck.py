"""
Brock Francom
A02052161
CS-1440
Erik Falor
10/17/2018
3: Bingo Cards
"""
import sys

import Card
import NumberSet

class Deck():
    def __init__(self, cardSize, cardCount, numberMax):
        self.__cardSize = cardSize
        self.__m_cardCount = cardCount
        self.__numberMax = numberMax
        
        self.__numberSet = NumberSet.NumberSet(numberMax)
        self.__numberSet.randomize()
        
        self.__m_cards = []
        self.CreateCards()
        
    #this function creates cards by passing in a subset of NumberSet, and it
    #also has the functionality to reshuffle the list and insert the free space 
    #if it is an odd size card. 
    def CreateCards(self):
        i = 1
        n = 0
        m = 0
        numberSet = []
        while i <= self.__m_cardCount:
            while n < self.__cardSize*self.__cardSize:
                try:
                    numberSet.append(self.__numberSet.get(m))
                except IndexError:
                    m = 0
                    self.__numberSet.randomize()
                    numberSet.append(self.__numberSet.get(m))
                m += 1
                n += 1
            if self.__cardSize % 2 != 0:
                middle = ((self.__cardSize*self.__cardSize) // 2)
                numberSet[middle] = "FREE!"
            card = Card.Card(i, self.__cardSize, numberSet)
            self.__m_cards.append(card)
            n = 0
            numberSet = []
            i += 1
    
    
    def getCardCount(self):
        """Return an integer: the number of cards in this deck"""
        return int(self.__m_cardCount)


    def getCard(self, n):
        """Return card N from the deck"""
        card = None
        n -= 1
        if 0 <= n < self.getCardCount():
            card = self.__m_cards[n]
        return card;


    def print(self, file=sys.stdout, idx=None):
        """void function: Print cards from the Deck

        If an index is given, print only that card.
        Otherwise, print each card in the Deck
        """
        if idx is None:
            for idx in range(1, self.__m_cardCount + 1):
                c = self.getCard(idx)
                c.print(file)
            print('', file=file)
        else:
            self.getCard(idx).print(file)

