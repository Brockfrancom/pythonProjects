"""
Brock Francom
A02052161
CS-1440
Erik Falor
10/24/2018
4: Mandelbrot Set Visualizer
"""
## Mandelbrot Set Visualizer
class Mandelbrot:
    def count(c, maxIterations):
        """Return the color of the current pixel within the Mandelbrot set"""
        z = complex(0, 0) # z0
        for i in range(maxIterations):
            z = z * z + c # Get z1, z2, ...
            if abs(z) > 2:
                return i # The sequence is unbounded
        return maxIterations - 1 # Indicate a bounded sequence
   
