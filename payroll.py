"""
Brock Francom
A02052161
CS-1400-001
Douglas Galarus
2/1/2018
hw Exercise 3.9 
"""


#get user inputs
name = input("Enter employee's name: ")
hours = eval(input("Enter number of hours worked in a week: "))
payRate = eval(input("Enter hourly pay rate: "))
fedTax = eval(input("Enter federal tax withholding rate: "))
stateTax = eval(input("Enter state tax withholding rate: "))

#calculate data
grossPay = hours * payRate
fedWith = grossPay * fedTax
stateWith = grossPay * stateTax
totalDeduction = fedWith + stateWith
netPay = grossPay - totalDeduction

#print payroll
"""
Some of these values like in lines 32, 34, and 36, are formated with one decimal
place showing. This is what it showed in the book and so I copied that exactally. 

"""
print("\nEmployee Name: " + name)
print("Hours Worked: " + format(hours, ".1f"))
print("Pay Rate: $" + format(payRate, ".2f"))
print("Gross Pay: $" + format(grossPay, ".1f"))
print("Deductions:")
print("  Federal Withholding (" + format((fedTax * 100), ".1f") + "%): $" + format(fedWith, ".1f"))
print("  State Withholding (" + format((stateTax * 100), ".1f") + "%): $" + format(stateWith, ".2f"))
print("  Total Deduction: $" + format(totalDeduction, ".2f"))
print("Net Pay: $" + format(netPay, ".2f"))





