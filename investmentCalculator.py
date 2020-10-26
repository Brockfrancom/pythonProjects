"""
Brock Francom
A02052161
CS-1400-001
Douglas Galarus
4/17/2018
hw13 - Exercise 9.2

"""

from tkinter import *

#function to calculate and display the future value
def calculateFutureValue(investmentAmountVar, yearsVar, annualInterestRateVar, window):
    investmentAmount = float(investmentAmountVar.get())
    monthlyInterestRate = ((float(annualInterestRateVar.get()) / 100) / 12)
    years = int(yearsVar.get())
    #calculate the future value
    futureValue = investmentAmount * ((1 + monthlyInterestRate)**(years * 12))
    #display the future value
    Label(window, text = str(format(futureValue, '10.2f'))).grid(row = 4, \
         column = 2, sticky = E)

def run():
    window = Tk()
    window.title("Investment Calculator")
    #create labels
    Label(window, text = "Investment amount").grid(row = 1, column = 1, sticky = W)
    Label(window, text = "Years").grid(row = 2, column = 1, sticky = W)
    Label(window, text = "Annual Interest Rate").grid(row = 3, column = 1, sticky = W)
    Label(window, text = "Future Value").grid(row = 4, column = 1, sticky = W)
    
    #create entry boxes
    investmentAmountVar = StringVar()
    Entry(window, textvariable = investmentAmountVar, justify = RIGHT).grid(row = 1, \
         column = 2)
    yearsVar = StringVar()
    Entry(window, textvariable = yearsVar, justify = RIGHT).grid(row = 2, column = 2)
    annualInterestRateVar = StringVar()
    Entry(window, textvariable = annualInterestRateVar, justify = RIGHT).grid(row = 3, \
         column = 2)
    
    #create a button to calculate total amount
    Button(window, text = "Calculate", command = lambda: func=calculateFutureValue(investmentAmountVar, yearsVar, annualInterestRateVar, window)).grid(row = 5, \
          column = 2, sticky = E)
    
    window.mainloop()
