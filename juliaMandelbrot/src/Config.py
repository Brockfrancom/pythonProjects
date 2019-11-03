"""
Brock Francom
A02052161
CS-1440
Erik Falor
10/24/2018
4: Julia/Mandelbrot Set Visualizer
Config - Functions and data responsible for reading a fractal configuration 
file and generating a configuration object which will control the other
parts of the program; a configuration object may be a Python class, but a 
simple dictionary is adequate
"""
class Config:
    def __init__(self):
       
        self.name = " "
        self.type = " "
        self.cReal = 0
        self.cImage = 0
        self.pixels = 0
        self.centerX = 0 
        self.centerY = 0
        self.axisLength = 0
        self.Iterations = 0

    def readAFile(self, inputfile):
        
        file = open(inputfile) #open file 
        filelist = file.readlines()
        
        self.name = inputfile.strip("../data/").strip(".frac")

        i = 0
        while i< len(filelist):
            if str(filelist[i].split(" ")[0]).strip().strip(":").lower() == 'type':
                self.type = filelist[i].split(" ")[1].strip()
            elif str(filelist[i].split(" ")[0]).strip().strip(":").lower() == 'creal':
                self.cReal = float(filelist[i].split(" ")[1])
            elif str(filelist[i].split(" ")[0]).strip().strip(":").lower() == 'cimage':
                self.cImage = float(filelist[i].split(" ")[1])
            elif str(filelist[i].split(" ")[0]).strip().strip(":").lower() == 'pixels':
                self.pixels = int(filelist[i].split(" ")[1])
            elif str(filelist[i].split(" ")[0]).strip().strip(":").lower() == 'centerx':
                self.centerX = float(filelist[i].split(" ")[1])
            elif str(filelist[i].split(" ")[0]).strip().strip(":").lower() == 'centery':
                self.centerY = float(filelist[i].split(" ")[1])
            elif str(filelist[i].split(" ")[0]).strip().strip(":").lower() == 'axislength':
                self.axisLength = float(filelist[i].split(" ")[1])
            elif str(filelist[i].split(" ")[0]).strip().strip(":").lower() == 'iterations':
                self.Iterations = int(filelist[i].split(" ")[1])
            i += 1
        print(self.type)

