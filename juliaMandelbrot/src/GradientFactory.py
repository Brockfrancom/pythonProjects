"""
Brock Francom
A02052161
CS-1440
Erik Falor
10/24/2018
4: Julia/Mandelbrot Set Visualizer
Gradient Factory
"""

import Color

class GradientFactory:
    
    def gradient(start, stop, steps):
        
        dRed = (stop.r - start.r)/ (steps-1)
        dGrn = (stop.g - start.g)/ (steps-1)
        dBlu = (stop.b - start.b)/ (steps-1)
        return list(
                map(lambda n: Color.Color( (n * dRed) + start.r,
                                     (n * dGrn) + start.g,
                                     (n * dBlu) + start.b).__str__(), range(steps)))

    def Greyscale(config):
        print("GradientFactory: Creating Greyscale color gradient")
        return GradientFactory.gradient(Color.Color(255, 255, 255), Color.Color(0, 0, 0), config.Iterations)
        
    def Christmas(config):
        print("GradientFactory: Creating Christmas color gradient")
        return GradientFactory.gradient(Color.Color(255, 0, 0), Color.Color(3, 236, 41), config.Iterations)
        
    def Party(config):
        return GradientFactory.gradient(Color.Color(0, 0, 255), Color.Color(255, 247, 0), config.Iterations)
        

    def makeGradient(grad, config):
        if grad == "Greyscale":
            return GradientFactory.Greyscale(config)
        elif grad == "Christmas":
            return GradientFactory.Christmas(config)
        else:
            if grad != None:
                print("GradientFactory: Unknown gradient '" + grad + "'; creating default color gradient")
            else:
                print("GradientFactory: Creating default color gradient")
            return GradientFactory.Party(config)
        
        
        
