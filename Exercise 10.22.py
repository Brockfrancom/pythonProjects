"""
Brock Francom
A02052161
CS-1400-001
Douglas Galarus
4/5/2018
hw11 - Exercise 10.22
"""

#Create a check to see if cards have different suits and if not, draw a new card.
import random
def Check():
    if s[0] == s[1] or s[0] == s[2] or s[0] == s[3]:
        s[0] = suits[deck[random.randint(0, 51)] // 13]
        r[0] = ranks[deck[random.randint(0, 51)] % 13]
        return False
    elif s[1] == s[2] or s[1] == s[3]:
        s[1] = suits[deck[random.randint(0, 51)] // 13]
        r[1] = ranks[deck[random.randint(0, 51)] % 13]
        return False
    elif s[2] == s[3]:
        s[2] = suits[deck[random.randint(0, 51)] // 13]
        r[2] = ranks[deck[random.randint(0, 51)] % 13]
        return False
    else:
        return True

#create a deck, and lists for suits and ranks
deck = list(range(0, 52))
suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', \
         'Queen', 'King']
#shuffle the deck
random.shuffle(deck)
#select 4 cards, and put them in 2 lists, one for suit and one for rank
s = []
r = []
for i in range(4):
    suit = suits[deck[i] // 13]
    rank = ranks[deck[i] % 13]
    s.append(suit)
    r.append(rank)
#pick cards until one from each suit is found, count number of iterations
m = False
count = 3 #min number of picks is 4, i.e. 3+1 = 4
while m != True:
    m = Check()
    count += 1
#print cards and number of picks
for i in range(4):
    print(r[i], "of", s[i])
print("Number of picks: ", count)





