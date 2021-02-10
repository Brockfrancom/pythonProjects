"""
Brock Francom
A02052161
CS-1400-001
Douglas Galarus
3/20/2018
hw10 - Exercise 8.3
"""
#check that length requirement is met
def check(password):
    l = len(password)
    if l >= 8:
        return "Valid"
#check that charecter digit requirement is met
def cd(password):
    k = 0
    for ch in password:
        if ch.isalnum() == True:
            k += 1
            if k == len(password):
                return "Valid"
#check that there is 2 number digits. 
def digit(password):
    k = 0
    for ch in password:
        if ch.isdigit() == True:
            k += 1
            if k == 2:
                return "Valid"
            
def run():            
    #user input
    password = input("Password: ")
    #the book did not specify to strip white spaces, but earlier it said it was a good 
    #practice to do so. Entering a password with spaces will fail unless they are at
    #the end of the password.
    password = password.strip()
    #print message if all conditions are met
    if check(password) and cd(password) and digit(password) == "Valid":
        print("valid password")
    else:
        print("invalid password")




















