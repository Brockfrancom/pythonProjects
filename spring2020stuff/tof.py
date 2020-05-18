#!/usr/bin/python

#################################################
# module: tof.py
# YOUR NAME
# YOUR A#
#################################################

from var import var
from pwr import pwr
from const import const
from plus import plus
from prod import prod
from var import var
from hw07_parser import parser

class tof(object):

    @staticmethod
    def const_tof(fr):
        """convert a const object to Py function."""
        assert isinstance(fr, const)
        return lambda x: fr.get_val()

    @staticmethod
    def var_tof(fr):
        """convert a var object to Py function."""
        assert isinstance(fr, var)
        return lambda x: x

    @staticmethod
    def prod_tof(fr):
        """convert a prod object to Py function."""
        assert isinstance(fr, prod)
        def f(x):
            f1 = tof.tof(fr.get_mult1())
            f2 = tof.tof(fr.get_mult2())
            return f1(x) * f2(x)
        return f

    @staticmethod
    def plus_tof(fr):
        """convert a plus object to a Py function."""
        assert isinstance(fr, plus)
        def f(x):
            f1 = tof.tof(fr.get_elt1())
            f2 = tof.tof(fr.get_elt2())
            return f1(x) + f2(x)
        return f

    @staticmethod
    def pwr_tof(fr):
        """convert a pwr object to a Py function."""
        assert isinstance(fr, pwr)
        b = fr.get_base()
        d = fr.get_deg()
        f = tof.tof(b)
        return lambda x: f(x)**d.get_val()

    @staticmethod
    def tof(fr):
        """convert a const/var/prod/plus/pwr/ object to a Py function."""
        if isinstance(fr, const):
            return tof.const_tof(fr)
        elif isinstance(fr, pwr):
            return tof.pwr_tof(fr)
        elif isinstance(fr, prod):
            return tof.prod_tof(fr)
        elif isinstance(fr, plus):
            return tof.plus_tof(fr)
        else:
            return tof.var_tof(fr)
    
