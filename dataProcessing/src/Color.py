"""
Brock Francom
A02052161
CS-1440
Erik Falor
10/24/2018
4: Julia/Mandelbrot Set Visualizer
Gradient - Generates colors
"""

class Color():
    """A class to represent RGB colors

    Use the setters to ensure color channel values stay within the accepted
    range of 0..255
                                                                            
    To-string functions express colors in PhotoImage-compatible hexidecimal
    #RRGGBB notation.
    """

    def __init__(self, r=0, g=0, b=0):
        self.setRed(r)
        self.setGreen(g)
        self.setBlue(b)

    def setRed(self, r):
        """Setter for Red color channel which ensures value is in-range"""
        if r < 0:
            self.r = 0
        elif r > 255:
            self.r = 255
        else:
            self.r = int(r)

    def setGreen(self, g):
        """Setter for Green color channel which ensures value is in-range"""
        if g < 0:
            self.g = 0
        elif g > 255:
            self.g = 255
        else:
            self.g = int(g)

    def setBlue(self, b):
        """Setter for Blue color channel which ensures value is in-range"""
        if b < 0:
            self.b = 0
        elif b > 255:
            self.b = 255
        else:
            self.b = int(b)

    def __str__(self):
        return f"#{self.r:02x}{self.g:02x}{self.b:02x}"

    def __repr__(self):
        return self.__str__()

