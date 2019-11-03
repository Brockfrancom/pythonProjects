"""
Brock Francom
A02052161
CS-1440
Erik Falor
11/28/2018
5: Julia/Mandelbrot Set Visualizer
User Manual
"""

This program is run through a command line interface. The syntax is main.py fractal.frac [gradient], 
where fractal.frac is the configuration file, and gradient is optional and 2 defined options are Greyscale and Christmas.

A configuration file is formatted like the following examples and can be Mandelbrot, Julia, or mandelbrot4. 

Mandelbrot:
type: Mandelbrot
pixels: 640
centerX: -0.761335372924805
centerY: 0.0835704803466797
axisLength: 0.00497817993164062
Iterations: 200

Julia:
type: Julia
cReal: -1
cImag: 0
pixels: 1024
centerX: -0.339230468501458
centerY: 0.417970758224314
axisLength: 0.164938488846612
Iterations: 32


Mandelbrot4:
type: Mandelbrot4
pixels: 640
centerX: -0.761335372924805
centerY: 0.0835704803466797
axisLength: 0.00497817993164062
Iterations: 200


