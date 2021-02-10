"""
Brock Francom
A02052161
CS-1440
Erik Falor
10/24/2018
4: Julia/Mandelbrot Set Visualizer
ImagePainter - Compute the color of each pixel of an image 
using one of the Fractal functions and size/position within 
the complex plane and display an image
"""
from tkinter import Tk, Canvas, PhotoImage, mainloop
import sys
import Color
from GradientFactory import GradientFactory
from FractalFactory import FractalFactory

class ImagePainter:
    
    def __init__(self):
        return None
    
    def paint(self, config, img, gradient):
        """
        This function displays a really handy status bar so you can see how far
        along in the process the program is."""
        # Figure out how the boundaries of the PhotoImage relate to coordinates on
        # the imaginary plane.
        minx = config.centerX - (config.axisLength / 2.0)
        maxx = config.centerX + (config.axisLength / 2.0)
        miny = config.centerY - (config.axisLength / 2.0)
        maxy = config.centerY + (config.axisLength / 2.0)
        imagesize = config.pixels
        
        # At this scale, how much length and height on the imaginary plane does one
        # pixel take?
        pixelsize = abs(maxx - minx) / imagesize
        portion = int(imagesize / 64)
        for col in range(imagesize):
            if col % portion == 0:
                # Update the status bar each time we complete 1/64th of the rows
                dots = col // portion
                percent = col / imagesize
                print(f"{config.name} ({imagesize}x{imagesize}) {'=' * dots}{'_' * (64 - dots)} {percent:.0%} ", end='\r', file=sys.stderr)
            for row in range(imagesize):
                x = minx + col * pixelsize
                y = miny + row * pixelsize
                count = FractalFactory.fractal(config.Iterations, config.type, x, y)
                color = gradient[count]
                img.put(color, (col, row))
        print(f"{config.name} ({imagesize}x{imagesize}) ================================================================ 100%", file=sys.stderr)
    
    
    def displayImage(self, config, grad):
        window = Tk()
        img = PhotoImage(width=config.pixels, height=config.pixels)
        gradient = GradientFactory.makeGradient(grad, config)
        self.paint(config, img, gradient)
        
        # Display the image on the screen
        canvas = Canvas(window, width=config.pixels, height=config.pixels, bg=Color.Color(255, 225, 225))
        canvas.pack()
        canvas.create_image((config.pixels/2, config.pixels/2), image=img, state="normal")
        
        # Save the image as a PNG
        img.write(config.name + ".png")
        print(f"Wrote image {config.name}.png")
        mainloop()
    
