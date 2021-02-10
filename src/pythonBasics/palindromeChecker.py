"""
Brock Francom
A02052161
CS-1400-001
Douglas Galarus
2/28/2018
Exercise 6.3
"""
import math

#reverse the number
def reverse(number):
#count the digits in number
    count = 0
    k = 1
    while (number // k != 0):
        count += 1
        k *= 10
    #reverse the number
    reverseNumber = 0
    while count > 0:
        k = int(k / 10)
        reverseNumber += int((number % 10) * (k))
        number = math.floor(reverseNumber + ((number / 10) % k))
        count -= 1
    return reverseNumber

#check if the number = the reverse
def isPalindrome(number):
    if reverse(number) == number: #call the reverse function
        print("True")
    else:
        print("False")
 
def run():    
    number = int(input("Enter a number: "))
    isPalindrome(number)























