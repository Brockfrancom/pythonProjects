"""
Brock Francom
A02052161
CS-1400-001
Douglas Galarus
3/14/2018
hw9 - Exercise 7.2
"""
#create class Stock
class Stock:
    def __init__(self, symbol, name, previousPrice, currentPrice):
        #create data feilds
        self.__symbol = symbol
        self.__name = name
        self.__previousClosingPrice = previousPrice
        self.__currentPrice = currentPrice
    def getName(self):#return name data feild
        return self.__name
    def getSymbol(self):#return symbol data feild
        return self.__symbol
    def getPreviousClosingPrice(self):#return previous closing price
        return self.__previousClosingPrice
    def setPreviousClosingPrice(self, previousClosingPrice):#set closing price
        self.__previousClosingPrice = previousClosingPrice
    def getCurrentPrice(self):#return current price
        return self.__currentPrice
    def setCurrentPrice(self, currentPrice):#set current price
        self.__currentPrice = currentPrice
    def getChangePercent(self):#calculate and return change percent
        return ((self.__currentPrice - self.__previousClosingPrice) \
                / self.__previousClosingPrice) * 100


#program to test Stock

#create object intc
intc = Stock("INTC", "Intel Corporation", 20.5, 20.35)
#print change percent, I formated this, but the book wasn't clear one way or
#the other.
print(format(intc.getChangePercent(), '5.5f'))



















