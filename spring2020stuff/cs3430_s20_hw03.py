#################################################
# module: cs3430_s20_hw03.py
# Brock Francom
# A02052161
##################################################

import numpy as np
import matplotlib.pyplot as plt
from cs3430_s20_hw01 import gje

## =============== Problem 01 ==================

def line_ip(line1, line2):
    A, B, C = line1
    D, E, F = line2
    ARRA = np.array([[A, B],[D, E]])
    ARRB = np.array([[C], [F]])
    intersection = gje(ARRA, ARRB)
    return intersection

def check_line_ip(line1, line2, ip, err=0.0001):
    A1, B1, C1 = line1
    A2, B2, C2 = line2
    x = ip[0, 0]
    y = ip[1, 0]
    assert abs((A1*x + B1*y) - C1) <= err
    assert abs((A2*x + B2*y) - C2) <= err

def find_line_ips(lines):
    ips = []
    for i in range(len(lines)):
        line = lines.pop(0)
        for j in range(len(lines)):
            ip = line_ip(line, lines[j])
            if ip != None:
                ips.append(ip)
    return ips

def max_obj_fun(f, cps):
    best = -1000000
    bestPoint = 0
    for point in cps:
        val = f(point[0], point[1])
        best = max(best, val)
        if best == val:
            bestPoint = point
    return bestPoint, int(best)

def min_obj_fun(f, cps):
    best = 1000000
    bestPoint = 0
    for point in cps:
        val = f(point[0], point[1])
        best = min(best, val)
        if best == val:
            bestPoint = point
    return bestPoint, int(best)

## ================= Problem 02 ===============================

### Sample solution to Ted's Toys Problem.
def plot_teds_constraints():
    ### plastic constraint: 4x + 3y <= 480
    def plastic_constraint(x): return -(4/3.0)*x + 160.0
    ### steel constraints: 3x + 6y <= 720
    def steel_constraint(x): return -0.5*x + 120.0
    xvals  = np.linspace(0, 160, 10000)
    yvals1 = np.array([plastic_constraint(x) for x in xvals])
    yvals2 = np.array([steel_constraint(x) for x in xvals])
    fig1   = plt.figure(1)
    fig1.suptitle('Ted\'s Toys Problem')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.ylim([-5, 160])
    plt.xlim([-5, 160])
    ## x = 0
    x1, y1 = [0, 0], [0, 160]
    ## y = 0
    x2, y2 = [0, 160], [0, 0]
    plt.grid()
    plt.plot(xvals, yvals1, label='4x+3y=480', c='red')
    plt.plot(xvals, yvals2, label='3x+6y=720', c='blue')
    plt.plot(x1, y1, label='x=0', c='green')
    plt.plot(x2, y2, label='y=0', c='yellow')
    plt.legend(loc='best')
    plt.show()

def teds_problem():
    red_line    = (4, 3, 480)
    blue_line   = (3, 6, 720)
    green_line  = (1, 0, 0)
    yellow_line = (0, 1, 0)
    cp1 = line_ip(green_line, yellow_line)
    cp2 = line_ip(green_line, blue_line)
    cp3 = line_ip(blue_line, red_line)
    cp4 = line_ip(red_line, yellow_line)
    obj_fun = lambda x, y: 5.0*x + 4.0*y
    rslt = max_obj_fun(obj_fun, [cp1, cp2, cp3, cp4])
    x = rslt[0][0][0]
    y = rslt[0][1][0]
    p = rslt[1]
    print('num cars   = {}'.format(x))
    print('num trucks = {}'.format(y))
    print('profit     = {}'.format(p))
    return x, y, p

def plot_2_1_constraints():
    ### plastic constraint: 4x + 3y <= 480
    def a_constraint(x): return -1*x + 3.0
    ### steel constraints: 3x + 6y <= 720
    def b_constraint(x): return 3*x + 1.0
    xvals  = np.linspace(-1, 10, 10)
    yvals1 = np.array([a_constraint(x) for x in xvals])
    yvals2 = np.array([b_constraint(x) for x in xvals])
    fig1   = plt.figure(1)
    fig1.suptitle('Ted\'s Toys Problem')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.ylim([-1, 10])
    plt.xlim([-1, 10])
    ## x = 0
    x1, y1 = [2, 2], [-1, 10]
    ## y = 0
    #x2, y2 = [-1, 10], [2, 2]
    plt.grid()
    plt.plot(xvals, yvals1, label='x+y=3', c='red')
    plt.plot(xvals, yvals2, label='3x-y=-1', c='blue')
    plt.plot(x1, y1, label='x=2', c='green')
    #plt.plot(x2, y2, label='y=0', c='yellow')
    plt.legend(loc='best')
    plt.show()

def problem_2_1():
    red_line    = (1., 1., 3.)
    blue_line   = (3., -1., -1.)
    green_line  = (1., 0., 2.)
    #yellow_line = (0, 1, 0)
    #cp1 = line_ip(green_line, yellow_line)
    cp2 = line_ip(green_line, blue_line)
    cp3 = line_ip(blue_line, red_line)
    cp4 = line_ip(red_line, green_line)
    obj_fun = lambda x, y: 3.0*x + 1.0*y
    rslt = max_obj_fun(obj_fun, [cp2, cp3, cp4])
    x = rslt[0][0][0]
    y = rslt[0][1][0]
    p = rslt[1]
    print('x   = {}'.format(x))
    print('y   = {}'.format(y))
    print('Max = {}'.format(p))
    return x, y, p

def plot_2_2_constraints():
    ### plastic constraint: x + 2y >= 6
    def a_constraint(x): return -(0.5)*x + 3.0
    ### steel constraints: x - y >= -4
    def b_constraint(x): return x + 4.0
    def c_constraint(x): return -2*x + 8.0
    xvals  = np.linspace(0, 100, 100)
    yvals1 = np.array([a_constraint(x) for x in xvals])
    yvals2 = np.array([b_constraint(x) for x in xvals])
    yvals3 = np.array([c_constraint(x) for x in xvals])
    fig1   = plt.figure(1)
    fig1.suptitle('Problem 2.2 constraints')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.ylim([-1, 10])
    plt.xlim([-1, 10])
    ## x = 0
    x1, y1 = [0, 0], [0, 20]
    ## y = 0
    x2, y2 = [0, 20], [0, 0]
    plt.grid()
    plt.plot(xvals, yvals1, label='x + 2y >= 6', c='red')
    plt.plot(xvals, yvals2, label='x - y >= -4', c='blue')
    plt.plot(xvals, yvals3, label='2x+y<=8', c='orange')
    plt.plot(x1, y1, label='x=0', c='green')
    plt.plot(x2, y2, label='y=0', c='yellow')
    plt.legend(loc='best')
    plt.show()

def problem_2_2():
    red_line    = (1., 2., 6.)
    blue_line   = (1., -1., -4.)
    orange_line   = (2., 1., 8.)
    green_line  = (1., 0., 0.)
    yellow_line = (0., 1., 0.)
    cp1 = line_ip(green_line, red_line)
    cp2 = line_ip(orange_line, blue_line)
    cp3 = line_ip(blue_line, green_line)
    cp4 = line_ip(red_line, orange_line)
    obj_fun = lambda x, y: 1.0*x + 1.0*y
    rslt = max_obj_fun(obj_fun, [cp1, cp2, cp3, cp4])
    x = rslt[0][0][0]
    y = rslt[0][1][0]
    p = rslt[1]
    print('x   = {}'.format(x))
    print('y   = {}'.format(y))
    print('Max = {}'.format(p))
    return x, y, p

def plot_2_3_constraints():
    ### calorie constraint: 3r + 6p <= 600
    def calorie_constraint(x): return -0.5*x + 100.0
    ### carb constraints: .8r + .2p <= 90
    def carb_constraint(x): return -4.0*x + 450.0
    xvals  = np.linspace(0, 200, 10000)
    yvals1 = np.array([calorie_constraint(x) for x in xvals])
    yvals2 = np.array([carb_constraint(x) for x in xvals])
    fig1   = plt.figure(1)
    fig1.suptitle('Problem 2.3 constraints')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.ylim([-5, 200])
    plt.xlim([-5, 200])
    ## x = 0
    x1, y1 = [0, 0], [0, 200]
    ## y = 0
    x2, y2 = [0, 200], [0, 0]
    plt.grid()
    plt.plot(xvals, yvals1, label='3r+6p=600', c='red')
    plt.plot(xvals, yvals2, label='.8r+.2p=90', c='blue')
    plt.plot(x1, y1, label='x=0', c='green')
    plt.plot(x2, y2, label='y=0', c='yellow')
    plt.legend(loc='best')
    plt.show()

def problem_2_3():
    red_line    = (3., 6., 600.)
    blue_line   = (.8, .2, 90.)
    green_line  = (1., 0., 0.)
    yellow_line = (0., 1., 0.)
    #cp1 = line_ip(green_line, yellow_line)
    cp2 = line_ip(green_line, blue_line)
    cp3 = line_ip(blue_line, red_line)
    cp4 = line_ip(red_line, yellow_line)
    obj_fun = lambda x, y: 4.0*x + 5.0*y
    rslt = min_obj_fun(obj_fun, [cp2, cp3, cp4])
    x = rslt[0][0][0]
    y = rslt[0][1][0]
    p = rslt[1]
    print('num raisins = {}'.format(x))
    print('num peanuts = {}'.format(y))
    print('cost        = {}'.format(p))
    return x, y, p

def plot_2_4_constraints():
    ### paper constraint: 2s+4h<=100000
    def paper_constraint(x): return -0.5*x + 25000.0
    ### hour constraints: (8/100)s+(3/100)h<=2400
    def hour_constraint(x): return ((-(8/100)*(100/3))*x + (240000.0/3))
    def manager_constraint(x): return 10000
    xvals  = np.linspace(0, 100000, 100000)
    yvals1 = np.array([paper_constraint(x) for x in xvals])
    yvals2 = np.array([hour_constraint(x) for x in xvals])
    yvals3 = np.array([manager_constraint(x) for x in xvals])
    fig1   = plt.figure(1)
    fig1.suptitle('Problem 2.4 constraints')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.ylim([-5, 30000])
    plt.xlim([-5, 55000])
    ## x = 0
    x1, y1 = [0, 0], [0, 50000]
    ## y = 0
    x2, y2 = [0, 50000], [0, 0]
    plt.grid()
    plt.plot(xvals, yvals1, label='2s+4h<=100000', c='red')
    plt.plot(xvals, yvals2, label='(8/100)s+(3/100)h<=2400', c='blue')
    plt.plot(xvals, yvals3, label='h>=10000', c='orange')
    plt.plot(x1, y1, label='x=0', c='green')
    plt.plot(x2, y2, label='y=0', c='yellow')
    plt.legend(loc='best')
    plt.show()

def problem_2_4():
    red_line    = (2., 4., 100000.)
    blue_line   = ((8/100), (3/100), 2400.)
    orange_line   = (0., 10000., 0.)
    green_line  = (1., 0., 0.)
    yellow_line = (0., 1., 0.)
    cp1 = line_ip(green_line, red_line)
    cp2 = line_ip(orange_line, blue_line)
    cp3 = line_ip(blue_line, red_line)
    cp4 = line_ip(green_line, orange_line)
    obj_fun = lambda x, y: 25.0*x + 50.0*y
    rslt = max_obj_fun(obj_fun, [cp1, cp2, cp3, cp4])
    x = rslt[0][0][0]
    y = rslt[0][1][0]
    p = rslt[1]
    print('num standard boxes   = {}'.format(x))
    print('num heavy-duty boxes = {}'.format(y))
    print('profit               = {}'.format(p))
    return x, y, p

##################################### Testing ################################
'''
line1 = (4.0,3.0,480.0)
line2 = (3.0,6.0,720.0)
print(line_ip(line1, line2))

line1 = (4.0,3.0,200.0)
line2 = (4.0,3.0,250.0)
print(line_ip(line1, line2))

line1 = (1.0, 0.0, 1.0)
line2 = (1.0, -2.0, 0.0)
line3 = (3.0, 4.0, 12.0)
ips = find_line_ips([line1, line2, line3])
print(ips)
    
line1 = (1.0, 0.0, 1.0)
line2 = (1.0, -2.0, 0.0)
line3 = (3.0, 4.0, 12.0)
f = lambda x, y: 10.0*x + 5.0*y
ips = find_line_ips([line1, line2, line3])
m = max_obj_fun(f, ips)
print(m)    
''' 
plot_2_1_constraints()
problem_2_1()

plot_2_2_constraints()
problem_2_2()
                    
plot_2_3_constraints()
problem_2_3()                    
plot_2_4_constraints()
problem_2_4()                    
'''    
'''