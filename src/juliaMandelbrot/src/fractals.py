"""
Brock Francom
A02052161
CS-1440
Erik Falor
10/24/2018
4: Julia/Mandelbrot Set Visualizer
main - Driver program
"""
from Config import Config
import sys
import ImagePainter

def run():
    try:
        config = Config()
        config.readAFile(sys.argv[1])
    except IndexError:
        print("Please specify a fractal configuration file as the first argument.")
        print("Usage: fractals.py CONFIG.frac GRADIENT")
        sys.exit()
    try:
        grad = sys.argv[2]
    except IndexError:
        grad = None
    
    img = ImagePainter.ImagePainter()
    img.displayImage(config, grad)
