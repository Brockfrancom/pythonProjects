#at the top of each document

"""
name
a-number
class section
instructor
date
description of project
"""

"""
Brock Francom
A02052161
CS-1400-001
Douglas Galarus
1/17/2018
hw2 - Calculate your score
"""

#radius of a circle given a radius
"""
PI = 3.14159

radius = eval(input("Enter value for radius: "))

area = radius * radius * PI

print("The area is", area)
"""
#time!!!
"""
import time
currentTime = time.time() #get current time
totalSeconds = int(currentTime)
currentSecond = totalSeconds % 60
totalMinutes = totalSeconds // 60
currentMinute = totalMinutes % 60
totalHours = totalMinutes // 60
currentHour = ((totalHours % 24) + 5) % 12 

print("The time is", currentHour,":",currentMinute,":",currentSecond)
"""

#if else statement
"""
testScore = eval(input("Test score "))
if testScore < 50:
    print("You fail at life.")
else:
    print("Good job.")
"""

#counter
"""
counter = 0
for count in range(1,20):
#      if count % 2 > 0 :

          print(count)
"""

#if else statement complicated
"""
#if you remove the following line, the object testScore remains as the last 
#entered value
testScore = eval(input("Test score: "))


if testScore >= 90:
    print("You are a nerd.")
else:
    if 80 <= testScore < 90:
        print("You are smart and got a B.")
    else:
        if 70 <= testScore < 80:
            print("You got a C.")
        else:
            print("You stink.")
"""

#if elif else
"""
#if you remove the following line, the object testScore remains as the last 
#entered value
testScore = eval(input("Test score: "))


if testScore >= 90:
    print("You are a nerd.")
elif 80 <= testScore < 90:
    print("You are smart and got a B.")
elif 70 <= testScore < 80:
    print("You got a C.")
else:
    print("You stink.")
"""

#Count
"""
count = 6
count = count + 2
count = count + 2
count = count + 2
count = count + 2
print(count)

while count < 100000:
    count = count + 2
    print(count)
    if count == 78:
        break
print("break")
"""

#time and schedule
"""
import time
currentTime = time.time() #get current time
totalSeconds = int(currentTime)
currentSecond = totalSeconds % 60
totalMinutes = totalSeconds // 60
currentMinute = totalMinutes % 60
totalHours = totalMinutes // 60
currentHour = ((totalHours % 24) + 5) % 12 

print("The time is", currentHour,":",currentMinute,":",currentSecond)

if currentHour == 2:
    print("Wake up")
else:
    print("sleep")
    print("sleep")
    print("sleep")
    print("sleep")
    print("sleep")

"""
#new lines
"""
print("Hello wacho\n\n\n\n\n\n")
"""

#turtle
"""
import turtle

turtle.penup()
turtle.goto(110,-25)
turtle.pendown()
turtle.circle(45)
turtle.pensize(17)

turtle.pensize(17)
turtle.write("hello")

turtle.done()

"""

#random integers
"""
import random
number1 = random.randint(0,10)
number2 = random.randint(0,10)

print(number1, "+", number2, "=")
answer1 = eval(input("Answer: "))

if answer1 == (number1 + number2):
    print("Way to be!")
else:
    print("Try again. :)")
    print(number1, "+", number2, "=")
    answer2 = eval(input("Answer: "))
    if answer2 == (number1 + number2):
        print("Way to be!")
    else:
        print("Wrong.")

"""

#guessing birthdays

"""
day = 0

question1 = "Is your birthday in Set 1?\n" + \
    " 1  3  5  7\n" + \
    " 9 11 13 15\n" + \
    "17 19 21 23\n" + \
    "25 27 29 31" + \
    "\nEnter 0 for No and 1 for Yes: "
answer = eval(input(question1))

if answer == 1:
    day += 1
    
question2 = "Is your birthday in Set 2?\n" + \
    " 2  3  6  7\n" + \
    "10 11 14 15\n" + \
    "18 19 22 23\n" + \
    "26 27 30 31" + \
    "\nEnter 0 for No and 1 for Yes: "
answer = eval(input(question2))

if answer == 1:
    day += 2
    
question3 = "Is your birthday in Set 3?\n" + \
    " 4  5  6  7\n" + \
    "12 13 14 15\n" + \
    "20 21 22 23\n" + \
    "28 29 30 31" + \
    "\nEnter 0 for No and 1 for Yes: "
answer = eval(input(question3))

if answer == 1:
    day += 4
    
question4 = "Is your birthday in Set 4?\n" + \
    " 8  9 10 11\n" + \
    "12 13 14 15\n" + \
    "24 25 26 27\n" + \
    "28 29 30 31" + \
    "\nEnter 0 for No and 1 for Yes: "
answer = eval(input(question4))

if answer == 1:
    day += 8

question5 = "Is your birthday in Set 5?\n" + \
    "16 17 18 19\n" + \
    "20 21 22 23\n" + \
    "24 25 26 27\n" + \
    "28 29 30 31" + \
    "\nEnter 0 for No and 1 for Yes: "
answer = eval(input(question5))

if answer == 1:
    day += 16

print("\nYour birthday is "+ str(day) + "!")

"""




"""
number1, number2, number3 = eval(input("enter the first #: \n" + \
                                       "enter the second #: \n" +\
                                       "enter the third #: "))
                                       
                                       
#number2 = eval(input("enter the second #: "))
#number3 = eval(input("enter the third #: "))
"""

#bmi calculator
"""
weightInPounds = eval(input("Enter weight in pounds: "))
heightInInches = eval(input("Enter your height in inches: "))

POUNDS_TO_KILOGRAMS = .45359237
INCHES_TO_METERS = .0254

weightInKilograms = weightInPounds * POUNDS_TO_KILOGRAMS
heightInMeters = heightInInches * INCHES_TO_METERS

bmi = weightInKilograms / (heightInMeters ** 2)

print(format(bmi, '.2f'))

if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")
"""

#rock paper sissors, how can I condense this code?
"""
rock = 0
paper = 1
scissors = 2

import random

computer = random.randint(0, 2)
user = random.randint(0, 2)

if computer == rock and user == rock:
    print("The computer chose rock and you chose rock. It is a tie.")
    computer = random.randint(0, 2)
    user = random.randint(0, 2)

    if computer == rock and user == rock:
        print("The computer chose rock and you chose rock. It is a tie.")
    elif computer == rock and user == paper:
        print("The computer chose rock and you chose paper. You win!")
    elif computer == rock and user == scissors:
        print("The computer chose rock and you chose scissors. You lose.")
    elif computer == paper and user == rock:
        print("The computer chose paper and you chose rock. You lose.")
    elif computer == paper and user == paper:
        print("The computer chose paper and you chose paper. It is a tie.")
    elif computer == paper and user == scissors:
        print("The computer chose paper and you chose scissors. You win!")
    elif computer == scissors and user == rock:
        print("The computer chose scissors and you chose rock. You win!")
    elif computer == scissors and user == paper:
        print("The computer chose scissors and you chose paper. You lose.")
    elif computer == scissors and user == scissors:
        print("The computer chose scissors and you chose scissors. It is a tie.")

elif computer == rock and user == paper:
    print("The computer chose rock and you chose paper. You win!")
elif computer == rock and user == scissors:
    print("The computer chose rock and you chose scissors. You lose.")
elif computer == paper and user == rock:
    print("The computer chose paper and you chose rock. You lose.")
elif computer == paper and user == paper:
    print("The computer chose paper and you chose paper. It is a tie.")
    computer = random.randint(0, 2)
    user = random.randint(0, 2)

    if computer == rock and user == rock:
        print("The computer chose rock and you chose rock. It is a tie.")
    elif computer == rock and user == paper:
        print("The computer chose rock and you chose paper. You win!")
    elif computer == rock and user == scissors:
        print("The computer chose rock and you chose scissors. You lose.")
    elif computer == paper and user == rock:
        print("The computer chose paper and you chose rock. You lose.")
    elif computer == paper and user == paper:
        print("The computer chose paper and you chose paper. It is a tie.")
    elif computer == paper and user == scissors:
        print("The computer chose paper and you chose scissors. You win!")
    elif computer == scissors and user == rock:
        print("The computer chose scissors and you chose rock. You win!")
    elif computer == scissors and user == paper:
        print("The computer chose scissors and you chose paper. You lose.")
    elif computer == scissors and user == scissors:
        print("The computer chose scissors and you chose scissors. It is a tie.")

elif computer == paper and user == scissors:
    print("The computer chose paper and you chose scissors. You win!")
elif computer == scissors and user == rock:
    print("The computer chose scissors and you chose rock. You win!")
elif computer == scissors and user == paper:
    print("The computer chose scissors and you chose paper. You lose.")
elif computer == scissors and user == scissors:
    print("The computer chose scissors and you chose scissors. It is a tie.")
    computer = random.randint(0, 2)
    user = random.randint(0, 2)

    if computer == rock and user == rock:
        print("The computer chose rock and you chose rock. It is a tie.")
    elif computer == rock and user == paper:
        print("The computer chose rock and you chose paper. You win!")
    elif computer == rock and user == scissors:
        print("The computer chose rock and you chose scissors. You lose.")
    elif computer == paper and user == rock:
        print("The computer chose paper and you chose rock. You lose.")
    elif computer == paper and user == paper:
        print("The computer chose paper and you chose paper. It is a tie.")
    elif computer == paper and user == scissors:
        print("The computer chose paper and you chose scissors. You win!")
    elif computer == scissors and user == rock:
        print("The computer chose scissors and you chose rock. You win!")
    elif computer == scissors and user == paper:
        print("The computer chose scissors and you chose paper. You lose.")
    elif computer == scissors and user == scissors:
        print("The computer chose scissors and you chose scissors. It is a tie.")


"""
#user input rock paper scissors
"""

rock = 0
paper = 1
scissors = 2

import random

user = eval(input("Rock (0), Paper (1), Scissors (2): "))
computer = random.randint(0, 2)

if computer == rock and user == rock:
    print("The computer chose rock and you chose rock. It is a tie.")
    user = eval(input("Rock (0), Paper (1), Scissors (2): "))
    computer = random.randint(0, 2)

    if computer == rock and user == rock:
        print("The computer chose rock and you chose rock. It is a tie.")
    elif computer == rock and user == paper:
        print("The computer chose rock and you chose paper. You win!")
    elif computer == rock and user == scissors:
        print("The computer chose rock and you chose scissors. You lose.")
    elif computer == paper and user == rock:
        print("The computer chose paper and you chose rock. You lose.")
    elif computer == paper and user == paper:
        print("The computer chose paper and you chose paper. It is a tie.")
    elif computer == paper and user == scissors:
        print("The computer chose paper and you chose scissors. You win!")
    elif computer == scissors and user == rock:
        print("The computer chose scissors and you chose rock. You win!")
    elif computer == scissors and user == paper:
        print("The computer chose scissors and you chose paper. You lose.")
    elif computer == scissors and user == scissors:
        print("The computer chose scissors and you chose scissors. It is a tie.")
elif computer == rock and user == paper:
    print("The computer chose rock and you chose paper. You win!")
elif computer == rock and user == scissors:
    print("The computer chose rock and you chose scissors. You lose.")
elif computer == paper and user == rock:
    print("The computer chose paper and you chose rock. You lose.")
elif computer == paper and user == paper:
    print("The computer chose paper and you chose paper. It is a tie.")
    user = eval(input("Rock (0), Paper (1), Scissors (2): "))
    computer = random.randint(0, 2)

    if computer == rock and user == rock:
        print("The computer chose rock and you chose rock. It is a tie.")
    elif computer == rock and user == paper:
        print("The computer chose rock and you chose paper. You win!")
    elif computer == rock and user == scissors:
        print("The computer chose rock and you chose scissors. You lose.")
    elif computer == paper and user == rock:
        print("The computer chose paper and you chose rock. You lose.")
    elif computer == paper and user == paper:
        print("The computer chose paper and you chose paper. It is a tie.")
    elif computer == paper and user == scissors:
        print("The computer chose paper and you chose scissors. You win!")
    elif computer == scissors and user == rock:
        print("The computer chose scissors and you chose rock. You win!")
    elif computer == scissors and user == paper:
        print("The computer chose scissors and you chose paper. You lose.")
    elif computer == scissors and user == scissors:
        print("The computer chose scissors and you chose scissors. It is a tie.")

elif computer == paper and user == scissors:
    print("The computer chose paper and you chose scissors. You win!")
elif computer == scissors and user == rock:
    print("The computer chose scissors and you chose rock. You win!")
elif computer == scissors and user == paper:
    print("The computer chose scissors and you chose paper. You lose.")
elif computer == scissors and user == scissors:
    print("The computer chose scissors and you chose scissors. It is a tie.")
    user = eval(input("Rock (0), Paper (1), Scissors (2): "))
    computer = random.randint(0, 2)

    if computer == rock and user == rock:
        print("The computer chose rock and you chose rock. It is a tie.")
    elif computer == rock and user == paper:
        print("The computer chose rock and you chose paper. You win!")
    elif computer == rock and user == scissors:
        print("The computer chose rock and you chose scissors. You lose.")
    elif computer == paper and user == rock:
        print("The computer chose paper and you chose rock. You lose.")
    elif computer == paper and user == paper:
        print("The computer chose paper and you chose paper. It is a tie.")
    elif computer == paper and user == scissors:
        print("The computer chose paper and you chose scissors. You win!")
    elif computer == scissors and user == rock:
        print("The computer chose scissors and you chose rock. You win!")
    elif computer == scissors and user == paper:
        print("The computer chose scissors and you chose paper. You lose.")
    elif computer == scissors and user == scissors:
        print("The computer chose scissors and you chose scissors. It is a tie.")


"""
#loop rock paper scissors
"""

import random

rock = 0
paper = 1
scissors = 2

user = eval(input("Rock (0), Paper (1), Scissors (2): "))
computer = random.randint(0, 2)

if computer == rock and user == paper:
    print("The computer chose rock and you chose paper. You win!")
elif computer == rock and user == scissors:
    print("The computer chose rock and you chose scissors. You lose.")
elif computer == paper and user == rock:
    print("The computer chose paper and you chose rock. You lose.")
elif computer == paper and user == scissors:
    print("The computer chose paper and you chose scissors. You win!")
elif computer == scissors and user == rock:
    print("The computer chose scissors and you chose rock. You win!")
elif computer == scissors and user == paper:
    print("The computer chose scissors and you chose paper. You lose.")
    

while computer == user:
    
    if computer == 0 and user == 0:
        print("The computer chose rock and you chose rock. It is a tie.")
    elif computer == 1 and user == 1:
        print("The computer chose paper and you chose paper. It is a tie.")
    elif computer == 2 and user == 2:
        print("The computer chose scissors and you chose scissors. It is a tie.")
    
    user = eval(input("Rock (0), Paper (1), Scissors (2): "))
    computer = random.randint(0, 2)

    
    if computer == rock and user == paper:
        print("The computer chose rock and you chose paper. You win!")
    elif computer == rock and user == scissors:
        print("The computer chose rock and you chose scissors. You lose.")
    elif computer == paper and user == rock:
        print("The computer chose paper and you chose rock. You lose.")
    elif computer == paper and user == scissors:
        print("The computer chose paper and you chose scissors. You win!")
    elif computer == scissors and user == rock:
        print("The computer chose scissors and you chose rock. You win!")
    elif computer == scissors and user == paper:
        print("The computer chose scissors and you chose paper. You lose.")
    
"""

#guessing a lottery #
"""
import random

lottery = random.randint(00, 99)

user = eval(input("Enter a number (2 digits): "))

lotteryDigit1 = lottery // 10
lotteryDigit2 = lottery % 10

userDigit1 = user // 10
userDigit2 = user % 10

if user == lottery:
    print("Exact match! You win $10,000!")
elif userDigit1 == lotteryDigit2 and userDigit2 == lotteryDigit1:
    print("Matched all digits! You win $3,000!")
elif userDigit1 == lotteryDigit1 or userDigit1 == lotteryDigit2 \
        or userDigit2 == lotteryDigit1 or userDigit2 == lotteryDigit2:
    print("Matched 1 digit. You win $1,000!")
else:
    print("Sorry no match.")
    
    
"""

#subtraction quiz

"""

import random
import time

startTime = time.time()
count = 0

continueLoop = 'Y'

while continueLoop == 'Y':
    count = 0
    while count < 3:
    
        num1 = random.randint(0, 10)
        num2 = random.randint(0, 10)
        
        if num1 < num2:
            num1, num2 = num2, num1
        
        answer = int(input(str(num1) + "-" + str(num2) + "= "))
    
        if answer == (num1 - num2):
            print("Correct!")
            count += 1
        else:
            while answer != num1 - num2:
                print("Try again.")
                answer = int(input(str(num1) + "-" + str(num2) + "= "))
                if answer == (num1 - num2):
                    print("Correct!")
                    count += 1

    continueLoop = input("Enter a Y to continue or a N to quit: ")
    if continueLoop == "y":
        continueLoop = 'Y'
        
endTime = time.time()

time = int(endTime - startTime)
print("You finished the test in " + str(time) + " seconds.")


"""
#isocolies triangle
"""
import turtle

turtle.circle(30, steps = 3)

turtle.done

"""

#recitation coins
"""
amount = eval(input("Enter an amount, for example, 11.56: "))

number = amount * 100

dollar = int(number // 100)
remainder = number % 100

quarter = int(remainder // 25)
remainder = number % 25

dime = int(remainder // 10)
remainder = number % 10

nickle = int(remainder // 5)
remainder = number % 5

penny = int(remainder // 1)

centSymbol = '\u00A2'

print("Your amount $" + str(amount) +" consists of:")
print("\t" + str(dollar) + "\tx\t$1")
print("\t" + str(quarter) + "\tx\t" + "25"  + centSymbol)
print("\t" + str(dime) + "\tx\t" + "10" + centSymbol)
print("\t" + str(nickle) + "\tx\t" + "5" + centSymbol)
print("\t" + str(penny) + "\tx\t" + "1" + centSymbol)
"""

#is the point in the circle?
"""
radius = eval(input("Enter a radius: "))
x,y = eval(input("Enter a point: "))

import turtle
turtle.penup()
turtle.right(90)
turtle.forward(radius)
turtle.left(90)
turtle.pendown()
turtle.circle(radius)
turtle.penup()
turtle.goto(x,y)
turtle.pendown()
turtle.circle(2)

d = (((x - 0)**2) + ((y - 0)**2))**.5
if d < radius:
    turtle.write("The point is in the circle.")
else:
    turtle.write("The point is not in the circle.")
    
turtle.done
"""

#future tuition
"""
tuition = 10000
year = 0
while tuition <= 20000:
    tuition += (tuition * .07)
    year += 1
print("The tuition will have doubled after " + str(year) + " years.")
print("The cost will be $" + str(format(tuition, '.2f')) + " after " + \
str(year) + " years.")
"""

#turtle random walk
"""
import turtle
import random


turtle.speed(50)
turtle.color("gray")
x = -80
for y in range(-80,80 + 1, 10):
    turtle.penup()    
    turtle.goto(x,y)
    turtle.pendown()
    turtle.forward(160)
    turtle.penup()

y = 80
turtle.right(90)
for x in range(-80,80 + 1, 10):
    turtle.penup()    
    turtle.goto(x,y)
    turtle.pendown()
    turtle.forward(160)
    turtle.penup()

turtle.pensize(3)
turtle.color('red')
turtle.home()
turtle.pendown()
turtle.speed(1)



x = y = 0
while abs(x) < 80 and abs(y) < 80:
    var = random.randint(0,3)
    if var == 0:
        turtle.setheading(0)
        turtle.forward(10)
        x += 10
        
        
    elif var == 1:
        
        turtle.setheading(270)
        turtle.forward(10)
        y += -10
    elif var == 2:
        

        turtle.setheading(180)
        turtle.forward(10)
        x += -10
    elif var == 3:
        

        turtle.setheading(90)
        turtle.forward(10)
        y += 10


turtle.done


"""
#draw a random card
"""
import random

number = random.randint(1,13)
suit = random.randint(1,4)

number2 = random.randint(1,13)
suit2 = random.randint(1,4)

while number2 == number and suit2 == suit:
    number2 = random.randint(1,13)
    suit2 = random.randint(1,4)

number3 = random.randint(1,13)
suit3 = random.randint(1,4)

count = 0
while number3 == number and suit3 == suit and suit3 == suit2 and number3 == number2:
    number3 = random.randint(1,13)
    suit3 = random.randint(1,4)
    count += 1
    print("count")
if suit == 1:
    if number == 1:
        print("Your card is the Ace of Spades")
    elif number == 2:
        print("Your card is the 2 of Spades")
    elif number == 3:
        print("Your card is the 3 of Spades")
    elif number == 4:
        print("Your card is the 4 of Spades")
    elif number == 5:
        print("Your card is the 5 of Spades")
    elif number == 6:
        print("Your card is the 6 of Spades")
    elif number == 7:
        print("Your card is the 7 of Spades")
    elif number == 8:
        print("Your card is the 8 of Spades")
    elif number == 9:
        print("Your card is the 9 of Spades")
    elif number == 10:
        print("Your card is the 10 of Spades")
    elif number == 11:
        print("Your card is the Jack of Spades")
    elif number == 12:
        print("Your card is the Queen of Spades")
    elif number == 13:
        print("Your card is the King of Spades")
if suit == 2:
    if number == 1:
        print("Your card is the Ace of Clubs")
    elif number == 2:
        print("Your card is the 2 of Clubs")
    elif number == 3:
        print("Your card is the 3 of Clubs")
    elif number == 4:
        print("Your card is the 4 of Clubs")
    elif number == 5:
        print("Your card is the 5 of Clubs")
    elif number == 6:
        print("Your card is the 6 of Clubs")
    elif number == 7:
        print("Your card is the 7 of Clubs")
    elif number == 8:
        print("Your card is the 8 of Clubs")
    elif number == 9:
        print("Your card is the 9 of Clubs")
    elif number == 10:
        print("Your card is the 10 of Clubs")
    elif number == 11:
        print("Your card is the Jack of Clubs")
    elif number == 12:
        print("Your card is the Queen of Clubs")
    elif number == 13:
        print("Your card is the King of Clubs")
if suit == 3:
    if number == 1:
        print("Your card is the Ace of Hearts")
    elif number == 2:
        print("Your card is the 2 of Hearts")
    elif number == 3:
        print("Your card is the 3 of Hearts")
    elif number == 4:
        print("Your card is the 4 of Hearts")
    elif number == 5:
        print("Your card is the 5 of Hearts")
    elif number == 6:
        print("Your card is the 6 of Hearts")
    elif number == 7:
        print("Your card is the 7 of Hearts")
    elif number == 8:
        print("Your card is the 8 of Hearts")
    elif number == 9:
        print("Your card is the 9 of Hearts")
    elif number == 10:
        print("Your card is the 10 of Hearts")
    elif number == 11:
        print("Your card is the Jack of Hearts")
    elif number == 12:
        print("Your card is the Queen of Hearts")
    elif number == 13:
        print("Your card is the King of Hearts")
if suit == 4:
    if number == 1:
        print("Your card is the Ace of Dimonds")
    elif number == 2:
        print("Your card is the 2 of Dimonds")
    elif number == 3:
        print("Your card is the 3 of Dimonds")
    elif number == 4:
        print("Your card is the 4 of Dimonds")
    elif number == 5:
        print("Your card is the 5 of Dimonds")
    elif number == 6:
        print("Your card is the 6 of Dimonds")
    elif number == 7:
        print("Your card is the 7 of Dimonds")
    elif number == 8:
        print("Your card is the 8 of Dimonds")
    elif number == 9:
        print("Your card is the 9 of Dimonds")
    elif number == 10:
        print("Your card is the 10 of Dimonds")
    elif number == 11:
        print("Your card is the Jack of Dimonds")
    elif number == 12:
        print("Your card is the Queen of Dimonds")
    elif number == 13:
        print("Your card is the King of Dimonds")

number = number2
suit = suit2

if suit == 1:
    if number == 1:
        print("Your card is the Ace of Spades")
    elif number == 2:
        print("Your card is the 2 of Spades")
    elif number == 3:
        print("Your card is the 3 of Spades")
    elif number == 4:
        print("Your card is the 4 of Spades")
    elif number == 5:
        print("Your card is the 5 of Spades")
    elif number == 6:
        print("Your card is the 6 of Spades")
    elif number == 7:
        print("Your card is the 7 of Spades")
    elif number == 8:
        print("Your card is the 8 of Spades")
    elif number == 9:
        print("Your card is the 9 of Spades")
    elif number == 10:
        print("Your card is the 10 of Spades")
    elif number == 11:
        print("Your card is the Jack of Spades")
    elif number == 12:
        print("Your card is the Queen of Spades")
    elif number == 13:
        print("Your card is the King of Spades")
if suit == 2:
    if number == 1:
        print("Your card is the Ace of Clubs")
    elif number == 2:
        print("Your card is the 2 of Clubs")
    elif number == 3:
        print("Your card is the 3 of Clubs")
    elif number == 4:
        print("Your card is the 4 of Clubs")
    elif number == 5:
        print("Your card is the 5 of Clubs")
    elif number == 6:
        print("Your card is the 6 of Clubs")
    elif number == 7:
        print("Your card is the 7 of Clubs")
    elif number == 8:
        print("Your card is the 8 of Clubs")
    elif number == 9:
        print("Your card is the 9 of Clubs")
    elif number == 10:
        print("Your card is the 10 of Clubs")
    elif number == 11:
        print("Your card is the Jack of Clubs")
    elif number == 12:
        print("Your card is the Queen of Clubs")
    elif number == 13:
        print("Your card is the King of Clubs")
if suit == 3:
    if number == 1:
        print("Your card is the Ace of Hearts")
    elif number == 2:
        print("Your card is the 2 of Hearts")
    elif number == 3:
        print("Your card is the 3 of Hearts")
    elif number == 4:
        print("Your card is the 4 of Hearts")
    elif number == 5:
        print("Your card is the 5 of Hearts")
    elif number == 6:
        print("Your card is the 6 of Hearts")
    elif number == 7:
        print("Your card is the 7 of Hearts")
    elif number == 8:
        print("Your card is the 8 of Hearts")
    elif number == 9:
        print("Your card is the 9 of Hearts")
    elif number == 10:
        print("Your card is the 10 of Hearts")
    elif number == 11:
        print("Your card is the Jack of Hearts")
    elif number == 12:
        print("Your card is the Queen of Hearts")
    elif number == 13:
        print("Your card is the King of Hearts")
if suit == 4:
    if number == 1:
        print("Your card is the Ace of Dimonds")
    elif number == 2:
        print("Your card is the 2 of Dimonds")
    elif number == 3:
        print("Your card is the 3 of Dimonds")
    elif number == 4:
        print("Your card is the 4 of Dimonds")
    elif number == 5:
        print("Your card is the 5 of Dimonds")
    elif number == 6:
        print("Your card is the 6 of Dimonds")
    elif number == 7:
        print("Your card is the 7 of Dimonds")
    elif number == 8:
        print("Your card is the 8 of Dimonds")
    elif number == 9:
        print("Your card is the 9 of Dimonds")
    elif number == 10:
        print("Your card is the 10 of Dimonds")
    elif number == 11:
        print("Your card is the Jack of Dimonds")
    elif number == 12:
        print("Your card is the Queen of Dimonds")
    elif number == 13:
        print("Your card is the King of Dimonds")

number = number3
suit = suit3

if suit == 1:
    if number == 1:
        print("Your card is the Ace of Spades")
    elif number == 2:
        print("Your card is the 2 of Spades")
    elif number == 3:
        print("Your card is the 3 of Spades")
    elif number == 4:
        print("Your card is the 4 of Spades")
    elif number == 5:
        print("Your card is the 5 of Spades")
    elif number == 6:
        print("Your card is the 6 of Spades")
    elif number == 7:
        print("Your card is the 7 of Spades")
    elif number == 8:
        print("Your card is the 8 of Spades")
    elif number == 9:
        print("Your card is the 9 of Spades")
    elif number == 10:
        print("Your card is the 10 of Spades")
    elif number == 11:
        print("Your card is the Jack of Spades")
    elif number == 12:
        print("Your card is the Queen of Spades")
    elif number == 13:
        print("Your card is the King of Spades")
if suit == 2:
    if number == 1:
        print("Your card is the Ace of Clubs")
    elif number == 2:
        print("Your card is the 2 of Clubs")
    elif number == 3:
        print("Your card is the 3 of Clubs")
    elif number == 4:
        print("Your card is the 4 of Clubs")
    elif number == 5:
        print("Your card is the 5 of Clubs")
    elif number == 6:
        print("Your card is the 6 of Clubs")
    elif number == 7:
        print("Your card is the 7 of Clubs")
    elif number == 8:
        print("Your card is the 8 of Clubs")
    elif number == 9:
        print("Your card is the 9 of Clubs")
    elif number == 10:
        print("Your card is the 10 of Clubs")
    elif number == 11:
        print("Your card is the Jack of Clubs")
    elif number == 12:
        print("Your card is the Queen of Clubs")
    elif number == 13:
        print("Your card is the King of Clubs")
if suit == 3:
    if number == 1:
        print("Your card is the Ace of Hearts")
    elif number == 2:
        print("Your card is the 2 of Hearts")
    elif number == 3:
        print("Your card is the 3 of Hearts")
    elif number == 4:
        print("Your card is the 4 of Hearts")
    elif number == 5:
        print("Your card is the 5 of Hearts")
    elif number == 6:
        print("Your card is the 6 of Hearts")
    elif number == 7:
        print("Your card is the 7 of Hearts")
    elif number == 8:
        print("Your card is the 8 of Hearts")
    elif number == 9:
        print("Your card is the 9 of Hearts")
    elif number == 10:
        print("Your card is the 10 of Hearts")
    elif number == 11:
        print("Your card is the Jack of Hearts")
    elif number == 12:
        print("Your card is the Queen of Hearts")
    elif number == 13:
        print("Your card is the King of Hearts")
if suit == 4:
    if number == 1:
        print("Your card is the Ace of Dimonds")
    elif number == 2:
        print("Your card is the 2 of Dimonds")
    elif number == 3:
        print("Your card is the 3 of Dimonds")
    elif number == 4:
        print("Your card is the 4 of Dimonds")
    elif number == 5:
        print("Your card is the 5 of Dimonds")
    elif number == 6:
        print("Your card is the 6 of Dimonds")
    elif number == 7:
        print("Your card is the 7 of Dimonds")
    elif number == 8:
        print("Your card is the 8 of Dimonds")
    elif number == 9:
        print("Your card is the 9 of Dimonds")
    elif number == 10:
        print("Your card is the 10 of Dimonds")
    elif number == 11:
        print("Your card is the Jack of Dimonds")
    elif number == 12:
        print("Your card is the Queen of Dimonds")
    elif number == 13:
        print("Your card is the King of Dimonds")

"""

"""
import math
number = int(input("Enter a number: "))
#global count
count = 0
#global k
k = 1
while (number // k != 0):
    count += 1
    k *= 10

def reverse(number):
    reverseNumber = 0
    global count
    while count > 0:
        global k
        k = int(k / 10)
        reverseNumber += int((number % 10) * (k))
        number = math.floor(reverseNumber + ((number / 10) % k))
        print(reverseNumber)
        count -= 1

    return reverseNumber


print(reverse(number))

"""
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

#check that all requirements are matched or not and return true if all are met
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


#get card number
number = int(input("Enter a card number: "))

#define function to count the size of number
def getSize(number):
    count = 0
    k = 1
    while ((int(number) // k) != 0):
        count += 1
        k *= 10
    return count

#get the first digits from number if they match the requirements
def getPrefix(number):
    count = getSize(number)
    prefix = (number // (10 ** (count - 1)))
    if prefix == 4 or prefix == 5 or prefix == 6:
        return prefix
    prefix = (number // (10 ** (count - 2)))
    if prefix == 37:
        return prefix

#return that the digits matched or not
def prefixMatched(number):
    prefix = getPrefix(number)
    if prefix == 4 or prefix == 5 or prefix == 6 or prefix == 37:
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

7
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

#check that all requirements are matched or not and return message
def isValid(number):
    if (13 <= getSize(number) <= 16) and (prefixMatched(number) == "True") \
    and (((sumOfOddPlace(number) + sumOfDoubleEvenPlace(number)) % 10) == 0):
        return "The card number you entered is valid."
    else:
        return "The card number you entered is not valid."

#call the main function and print result
print(isValid(number))

"""
"""
hex = ""
# Convert a decimal to a hex as a string
def decimalToHex(decimalValue):
    hex = ""
    while decimalValue != 0:
        hexValue = decimalValue % 16
        hex = toHexChar(hexValue) + hex
        decimalValue = decimalValue // 16
    
    return hex
    

# Convert an integer to a single hex digit as a character
def toHexChar(hexValue):
    if 0 <= hexValue <= 9:
        return chr(hexValue + ord('0'))
    else:
        return chr(hexValue - 10 + ord('A'))

def main():
    decimalValue = eval(input("Enter a decimal number: "))

    print("The hex number for decimal",
        decimalValue, "is", decimalToHex(decimalValue))


main()  # Call the main function
"""

"""
from tkinter import *

class Click():
    def __init__(self):
        
        window = Tk()
        window.title("Clicking buttons")
        self.width = 350
        self.height = 100
        self.canvas = Canvas(window, bg = 'white', width = self.width, \
        height = self.height)
        self.canvas.pack()
        def processOK():
            print("Ok button is clicked")
            
        def processCancel():
            print("Cancel button is clicked")
        


        btOK = Button(window, text = "OK", fg = "red", command = processOK)
        btOK.pack()
        btCancel = Button(window, text = "Cancel", fg = "blue", command = processCancel)
        btCancel.pack()
        window.mainloop()
Click()
"""
"""

from tkinter import *

class Ball:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.dx = 2
        self.dy = 2
        self.radius = 2
        
window = Tk()
window.title("Balls")
m = Ball()






window.mainloop()
"""
#hex to decimal
"""
def main():
    hex = input("Enter a hex number: ").strip()

    decimal = hexToDecimal(hex.upper())
    if decimal == None:
        print("Incorrect hex number")
    else:
        print("The decimal value for hex number", hex, "is", decimal)


# Converts a hexadecimal string to a decimal number
# Valid hex returns decimal, invalid hex returns None
def hexToDecimal(hex):
        m = 0
        i = len(hex)
        for ch in hex:
            if '0' <= ch <= '9' or 'A' <= ch <= 'F':
                a = hexCharToDecimal(ch)
                m += (a * (16 ** i))
                i -= 1
                return m
            else:
                return None

# Converts a hexadecimal character to a decimal number.
def hexCharToDecimal(ch):
    if '0' <= ch <= '9':
        return ord(ch)
    elif ch == 'A':
        return 10
    elif ch == 'B':
        return 11
    elif ch == 'C':
        return 12
    elif ch == 'D':
        return 13
    elif ch == 'E':
        return 14
    else:
        return 15
    
        

if __name__ == '__main__':
    main()
"""

"""
things to record: operators

range() always 1 less than end 

When you invoke a function with a parameter, the value of the argument is 
passed to the parameter. This is referred to as _________.
 B. pass by value
 
 8.5 	What is "Programming is fun"[-1]?
 A. Pr
 B. P
 C. fun
 D. n
 E. un

Your answer is correct  
8.6 	What is "Programming is fun"[1:1]?
 A. P
 B. r
 C. Pr
 D. ''
 E. incorrect expression

Your answer is correct  
8.7 	What is "Programming is fun"[-3:-1]?
 A. Pr
 B. P
 C. fun
 D. n
 E. un

Your answer is correct  
8.8 	What is "Programming is fun"[:-1]?
 A. Programming
 B. rogramming is fun
 C. Programming is f
 D. Programming is fu
 E. Programming is 
 




"""
"""
number = 25
isPrime = True
i = 2 
while i < number and isPrime:
    if number % i == 0:
        isPrime = False

    i += 1

print("i is", i, "isPrime is", isPrime)
"""
#lotto tickets
"""
isCovered = 99 * [False]
endOfInput = False
while not endOfInput:
    m = input("Enter a string of numbers seperated by spaces: ").split()
    integers = [eval(i) for i in m]
    for k in integers:
        if k == 0:
            endOfInput = True
        else:
            isCovered[k - 1] = True
    
allCovered = True
for i in isCovered:
    if not isCovered[i]:
        allCovered = False
        break
if allCovered:
    print("The tickets cover all numbers")
else:
    print("The tickets don't cover all numbers")
"""

"""
number = 0
while number < slots:
    i = countlst.count(number)
    if i == 0:
        print(number + 1, '-')
    else:
        print(number + 1, ('0' * i))
    number += 1
"""
"""
from collections import *
print(Counter(countlst))
"""
"""
matrix = [
        [1, 2, 3, 4],
        [5, 8, 67, 22]
        ]


print(matrix[1][3])


matrix = []

numberOfRows = eval(input("Enter # of rows: "))
numberOfColumns = eval(input("Enter # of columns: "))
for row in range(numberOfRows):
    matrix.append([])
    for column in range(numberOfColumns):
        value = eval(input("Enter a value: "))
        matrix[row].append(value)

print(matrix)                       
"""
"""
import random

matrix = []

numberOfRows = eval(input("Enter # of rows: "))
numberOfColumns = eval(input("Enter # of columns: "))
for row in range(numberOfRows):
    matrix.append([])
    for column in range(numberOfColumns):
        matrix[row].append(random.randint(0, 99))

print(matrix)                       
"""
"""                     
matrix = []
matrix.append([3, 2, 2, 3])
matrix.append([3, 5, 3, 4])
matrix.append([3, 3, 3, 3])
matrix.append([3, 7, 9, 5])

for row in matrix:
    for value in row:
        print(value, end = ' ')
    print()                             



for row in range(len(matrix)):
    for value in row:
        
        count = 0
        m = value
        r = 0
        for i in range(0, len(matrix)):
            
            k = matrix[i][row]
            if m == matrix[i][row]:
                count += 1
                r += 1
            if count == 4:
                print(m)
                break
"""
def readMatrix(nRows, nCols):
    matrix = [] 
    for r in range(nRows):
        matrix.append([]) # Add an empty new row
        for c in range(nCols):
            value = input("Enter an element and press Enter: ")
            matrix[r].append(value)
    return matrix




class WinChecker:

    def __init__(self, game, board):
        self.game = game
        self.board = board

    def check_for_win(self):
        results = []
        results.append(self.check_win_horizontally())
        results.append(self.check_win_vertically())
        results.append(self.check_win_diagonally())
        try:
            win = results.index(True)
            # if the above statement does not generate a ValueError, then a 
            #win exists
            return True
        except ValueError:
            return False

    def check_win_horizontally(self):
        win = False

        for i in range(self.board.rows):
            row = i
            cols = [0, 1, 2, 3]
            while not win:
                try:
                    # seq will represent the current 4 squares being examined
                    seq = []
                    for i in range(len(cols)):
                        # append current 4 squares to seq list
                        seq.append(self.board.board[row][cols[i]])
                    if self.check_equal(seq):
                        return True
                    else:
                        # increment each value in cols, this is how the horizontal
                        # win checking progresses from left to right
                        for i in range(len(cols)):
                            cols[i] += 1
                        continue
                except IndexError:
                    # we've hit the end of this row, break the loop and move to the next row
                    break
        return win

    def check_win_vertically(self):
        win = False

        for i in range(self.board.cols):
            col = i
            rows = [0, 1, 2, 3]
            while not win:
                try:
                    # seq will represent the current 4 squares being examined
                    seq = []
                    for i in range(len(rows)):
                        # append current 4 squares to seq list
                        seq.append(self.board.board[rows[i]][col])
                    if self.check_equal(seq):
                        return True
                    else:
                        # increment each value in rows, this is how the horizontal
                        # win checking progresses from top to bottom
                        for i in range(len(rows)):
                            rows[i] += 1
                        continue
                except IndexError:
                    # we've hit the end of this col, break the loop and move to the next col
                    break

        return win

    def check_win_diagonally(self):
        win = False

        for i in range(self.board.cols):
            col = i
            cols = [col, col+1, col+2, col+3]
            rows = [0, 1, 2, 3]
            while not win:
                try:
                    # seq will represent the current 4 squares being examined
                    seq = []
                    for i in range(len(rows)):
                        # append current 4 squares to seq list
                        seq.append(self.board.board[rows[i]][cols[i]])
                    if self.check_equal(seq):
                        return True
                    else:
                        # increment each value in rows, this is how the diagonal
                        # win checking progresses from top to bottom
                        for i in range(len(rows)):
                            rows[i] += 1
                        continue
                except IndexError:
                    # we've hit the end of this col, break the loop and move to the next col
                    break

        return win

    def check_equal(self, lst):
        return lst[1:] == lst[:-1] if lst[0] != self.board.NONE else False

nRows = eval(input("Enter the number of rows: "))
nCols = eval(input("Enter the number of columns: "))
board = readMatrix(nRows, nCols)
win = WinChecker(1, board)
print(win)



