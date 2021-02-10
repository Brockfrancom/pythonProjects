"""
Brock Francom
A02052161
CS-1400-001
Douglas Galarus
2/8/2018
hw Exercise 4.17
"""
import random

def run():
    scissors = 0
    rock = 1
    paper = 2
    
    #user input and random number
    user = eval(input("scissor (0), rock (1), paper (2): "))
    computer = random.randint(0, 2)
    
    #print win or loss or tie
    if computer == rock and user == paper:
        print("The computer is rock. You are paper. You won.")
    elif computer == rock and user == scissors:
        print("The computer is rock. You are scissors. You lose.")
    elif computer == paper and user == rock:
        print("The computer is paper. You are rock. You lose.")
    elif computer == paper and user == scissors:
        print("The computer is paper. You are scissors. You won.")
    elif computer == scissors and user == rock:
        print("The computer is scissors. You are rock. You won.")
    elif computer == scissors and user == paper:
        print("The computer is scissors. You are paper. You lose.")
    elif computer == 0 and user == 0:
        print("The computer is scissor. You are scissor too. It is a draw.")
    elif computer == 1 and user == 1:
        print("The computer is rock. You are rock too. It is a draw.")
    elif computer == 2 and user == 2:
        print("The computer is paper. You are paper too. It is a draw.")
  