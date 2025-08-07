"""
Brock Francom
A02052161
CS-1440
Erik Falor
10/24/2018
4: Julia/Mandelbrot Set Visualizer
Fractal Factory
"""

import mandelbrot
import Mandelbrot4
import julia
class FractalFactory:
    def count():
        pass
    
    def fractal(iterations, Type, x, y):
        if Type == 'Julia':
            return julia.Julia.count(complex(x, y), iterations)
        elif Type =='Mandelbrot':
            return mandelbrot.Mandelbrot.count(complex(x, y), iterations)
        elif Type == "Mandelbrot4":
            return Mandelbrot4.Mandelbrot4.count(complex(x, y), iterations)

