"""
Brock Francom
A02052161
CS-1400-001
Douglas Galarus
2/28/2018
Exercise 6.29
"""
#get card number
number = int(input("Enter a card number: "))

#define function to count the size of number and return answer in d
def getSize(d):
    d = 0
    k = 1
    while ((int(number) // k) != 0):
        d += 1
        k *= 10
    return d

#get the first digits from number if they match the requirements and return in k
def getPrefix(number, d):
    count = getSize(d)
    k = (number // (10 ** (count - 1)))
    if k == 4 or k == 5 or k == 6:
        return k
    else:
        return number
    k = (number // (10 ** (count - 2)))
    if k == 37:
        return k
    else:
        return number
    
#return that the digits matched a prefix
def prefixMatched(number, d):
    k = getPrefix(number, d)
    if k == 4 or k == 5 or k == 6 or k == 37:
        return 'True'
    else:
        return 'False'
    
#sum the digits in the odd places of number
def sumOfOddPlace(number):
    count = getSize(number)
    odd = 0
    if (count % 2) != 0:
        while count > 0:
            odd += int((number // (10 ** (count-1))) % 10)
            count -= 2
        return odd
    else:
        count = count - 1
        while count > 0:
            odd += int((number // (10 ** (count-1))) % 10)
            count -= 2
        return odd

#get the digit in the evens places
def getDigit(number):
    count = getSize(number)
    if (count % 2) != 0:
        count -= 1  
    while count > 0:
        k = ((int((number // (10 ** (count - 1))) % 10)) * 2)
        if k >= 10:
            k = (k // 10) + (k % 10)
        count -= 2
    return k

#add the double evens together and if it is over 10 the sum of the 2 digits
def sumOfDoubleEvenPlace(number):
    count = getSize(number)
    if (count % 2) != 0:
        count -= 1  
    even = 0
    while count > 0:
        k = ((int((number // (10 ** (count - 1))) % 10)) * 2)
        if k >= 10:
            k = (k // 10) + (k % 10)
        even += k
        count -= 2
    return even

#check that all requirements are matched or not by calling all the functions 
#and return true if all are met
def isValid(number):
    if (13 <= getSize(number) <= 16) and \
    (prefixMatched(number, getPrefix(number, getSize(number))) == "True") and \
    (((sumOfOddPlace(number) + sumOfDoubleEvenPlace(number)) % 10) == 0):
        return 'True'
    else:
        return 'False'

#call the main function and print result if true
if isValid(number) == 'True':
    print("The card number you entered is valid.")
else:
    print("The card number you entered is not valid.")





