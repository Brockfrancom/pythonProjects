"""
Brock Francom
A02052161
CS-1400-001
Douglas Galarus
1/17/2018
hw10 - Exercise 8.18
"""

import math
#create circle2D class
class Circle2D:
    def __init__(self, x = 0, y = 0, radius = 0):
        self.__x = x
        self.__y = y
        self.__radius = radius
    def getX(self):
        return self.__x
    def getY(self):
        return self.__y
    def setX(self, x):
        self.__x = x
    def setY(self, y):
        self.__y == y
    def getRadius(self):
        return self.__radius
    def setRadius(self, radius):
        self.__radius = radius
    def getArea(self):
        return (math.pi * (self.__radius * self.__radius))
    def getPerimeter(self):
        return (2 * math.pi * self.__radius)
    def containsPoint(self, x, y):
        a = self.__x - x
        b = self.__y - y 
        c = math.sqrt((a ** 2) + (b ** 2))
        if c <= self.__radius:
            return True
        else:
            return False
    def contains(self, circle2D):
        a = self.__x - circle2D.__x
        b = self.__y - circle2D.__y 
        c = math.sqrt((a ** 2) + (b ** 2))
        circle2D = circle2D.getRadius()
        if c + circle2D <= self.__radius:
            return True
        else:
            return False
    def overlaps(self, circle2D):
        a = self.__x - circle2D.__x
        b = self.__y - circle2D.__y 
        c = math.sqrt((a ** 2) + (b ** 2))
        r1 = self.__radius
        r2 = circle2D.getRadius()
        if c <= (r1 + r2):
            return True
        else:
            return False
#operator overloading:        
    def __contains__(self, another):
        a = self.__x - another.__x
        b = self.__y - another.__y 
        c = math.sqrt((a ** 2) + (b ** 2))
        another = another.getRadius()
        if c + another >= self.__radius:
            return True
        else:
            return False
    def __cmp__(self, another):
        a = self.__radius
        b = another.getRadius()
        if a == b:
            return 0
        elif a > b:
            return 1
        else:
            return -1
    def __lt__(self, another):
        a = self.__radius
        b = another.getRadius()
        if a < b:
            return True
        else:
            return False
    def __le__(self, another):
        a = self.__radius
        b = another.getRadius()
        if a <= b:
            return True
        else:
            return False
    def __eq__(self, another):
        a = self.__radius
        b = another.getRadius()
        if a == b:
            return True
        else:
            return False
    def __ne__(self, another):
        a = self.__radius
        b = another.getRadius()
        if a != b:
            return True
        else:
            return False
    def __gt__(self, another):
        a = self.__radius
        b = another.getRadius()
        if a > b:
            return True
        else:
            return False
    def __ge__(self, another):
        a = self.__radius
        b = another.getRadius()
        if a >= b:
            return True
        else:
            return False
    
#test program
def main():
    #user input, I asked the professor and he said the white space before the 
    #inputs was ok.
    x1, y1, radius1 = eval(input("Enter x1, y1, radius1: "))
    c1 = Circle2D(x1, y1, radius1)
    x2, y2, radius2 = eval(input("Enter x2, y2, radius2: "))
    c2 = Circle2D(x2, y2, radius2)
    #print messages
    print("Area for c1 is ", c1.getArea())
    print("Perimeter for c1 is ", c1.getPerimeter())
    print("Area for c2 is ", c2.getArea())
    print("Perimeter for c2 is ", c2.getPerimeter())
    print("c1 contains the center of c2? ", c1.containsPoint(c2.getX(), c2.getY()))
    print("c1 contains c2? ", c1.contains(c2))
    print("c1 overlaps c2? ", c1.overlaps(c2))
    
    #Uncomment these to test the operator overloading:
    """
    print(c1 in c2)
    print(c1.__cmp__(c2))
    print(c1 < c2)
    print(c1 <= c2)
    print(c1 == c2)
    print(c1 != c2)
    print(c1 > c2)
    print(c1 >= c2)
    """
    
def run():
    #call the test program   
    main()



























