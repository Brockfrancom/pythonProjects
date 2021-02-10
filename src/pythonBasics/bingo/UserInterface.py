"""
Brock Francom
A02052161
CS-1440
Erik Falor
10/17/2018
3: Bingo Cards
"""
import Deck
import Menu

class UserInterface():
    def __init__(self):
        self.__cardSize = 0
        self.__maxNum = 0
        self.__numCards = 0
        self.__m_currentDeck = 0

    def run(self):
        """Present the main menu to the user and repeatedly prompt for a valid command"""
        print("Welcome to the Bingo! Deck Generator\n")
        menu = Menu.Menu("Main")
        menu.addOption("C", "Create a new deck")
        
        keepGoing = True
        while keepGoing:
            command = menu.show()
            if command == "C":
                UserInterface.__createDeck(self)
            elif command == "X":
                keepGoing = False


    def __createDeck(self):
        """Command to create a new Deck"""
        # TODO: Get the user to specify the card size, max number, and number of cards
        self.__cardSize, self.__maxNum, self.__numCards = input("Enter the card size, max number, and number of cards seperated by spaces: ").split(" ")
        if (3 <= int(self.__cardSize) <= 15) != True:
            print("\nCard size value not allowed.")
            return None
        elif (3 <= int(self.__numCards) <= 10000)!= True:
            print("\nNumber of cards value not allowed.")
            return None
        elif (2*(int(self.__cardSize) **2) <= int(self.__maxNum) <= (4*(int(self.__cardSize) **2))) != True:
            print("\nMax number value not allowed.")
            return None
        else:
            pass
        # TODO: Create a new deck
        self.__m_currentDeck = Deck.Deck(int(self.__cardSize), int(self.__numCards), int(self.__maxNum))
        # TODO: Display a deck menu and allow user to do things with the deck
        UserInterface.__deckMenu(self)


    def __deckMenu(self):
        """Present the deck menu to user until a valid selection is chosen"""
        menu = Menu.Menu("Deck")
        menu.addOption("P", "Print a card to the screen");
        menu.addOption("D", "Display the whole deck to the screen");
        menu.addOption("S", "Save the whole deck to a file");

        keepGoing = True
        while keepGoing:
            command = menu.show()
            if command == "P":
                self.__printCard()
            elif command == "D":
                print()
                self.__m_currentDeck.print()
            elif command == "S":
                self.__saveDeck()
            elif command == "X":
                keepGoing = False

    def __getNumberInput(self, string, number, deck):
        cardToPrint = int(input(string))
        return cardToPrint
        
    def __getStringInput(self, string):
        fileName = input(string)
        return fileName
        
        
        
    def __printCard(self):
        """Command to print a single card"""
        cardToPrint = self.__getNumberInput("Id of card to print", 1, self.__m_currentDeck.getCardCount())
        if cardToPrint > 0:
            print()
            self.__m_currentDeck.print(idx=cardToPrint)


    def __saveDeck(self):
        """Command to save a deck to a file"""
        fileName = self.__getStringInput("Enter output file name")
        if fileName != "":
            # TODO: open a file and pass to currentDeck.print()
            
            outputStream = open(fileName, 'w')
            self.__m_currentDeck.print(outputStream)
            outputStream.close()
            print("Done!")
