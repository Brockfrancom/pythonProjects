"""
Brock Francom
A02052161
CS-1400-001
Douglas Galarus
3/1/2018
hw8 - Exercise 6.14
"""

#function to find pi for a given i
def m(i):
    m = 0
    z = 0
    while i > z:
        m += 4 * ((((-1) ** (i + 1)) / ((2 * i) - 1)))
        i -= 1
    return m

#print table header
print("i\t\t  m(i)\n")

#print table
i = 1
while i < 1000: 
    print(i, '\t\t', format(round(m(i), 4), '5.4f'))
    i += 100






























