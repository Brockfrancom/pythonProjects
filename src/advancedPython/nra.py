
#############################################
# Module: nra.py
# Description: Newton-Raphson Algorithm
#############################################

import numpy as np
import math
from maker import maker
from pwr import pwr
from prod import prod
from var import var
from const import const
from plus import plus
from drv import drv
from hw06_parser import parser
from tof import tof

class nra(object):

    @staticmethod
    def zr1(fstr, x0, num_iters=3):
        if num_iters == 0:
            return x0
        f = tof.tof((parser.parse_sum(fstr)))
        fprime = tof.tof(drv.drv(parser.parse_sum(fstr)))
        val = x0 - (f(x0)/fprime(x0))
        return nra.zr1(fstr, val, num_iters-1)

    @staticmethod
    def zr2(fstr, x0, delta=0.0001):
        f = tof.tof((parser.parse_sum(fstr)))
        fprime = tof.tof(drv.drv(parser.parse_sum(fstr)))
        oldVal = 0 
        newVal = x0
        numIters = 0
        while(abs(newVal - oldVal) > delta):
            oldVal = newVal
            newVal = newVal - (f(newVal)/fprime(newVal))
            numIters += 1
        return newVal, numIters

    @staticmethod
    def check_zr(fstr, zr, err=0.0001):
        return abs(tof.tof(parser.parse_sum(fstr))(zr) - 0.0) <= err 
