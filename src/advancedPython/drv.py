###############################################
# module: drv.py
# module: a simple differentiation engine
###############################################

import numpy as np
import math
from maker import maker
from pwr import pwr
from prod import prod
from var import var
from const import const
from plus import plus

class drv(object):

    @staticmethod
    def drv(expr):
        if isinstance(expr, const):
            return drv.drv_const(expr)
        elif isinstance(expr, pwr):
            return drv.drv_pwr(expr)
        elif isinstance(expr, prod):
            return drv.drv_prod(expr)
        elif isinstance(expr, plus):
            return drv.drv_plus(expr)
        else:
            raise Exception('drv:' + str(expr))

    @staticmethod
    def drv_const(expr):
        return maker.make_const(0)

    @staticmethod
    def drv_pwr(expr):
        b = expr.get_base()
        d = expr.get_deg()
        assert (isinstance(b, pwr) and b.get_deg().get_val() == 1.0) or \
            (isinstance(b, var))
        assert isinstance(d, const)
        return maker.make_prod(maker.make_const(1),maker.make_pwr(b.get_name(),d.get_val()-1))

    @staticmethod
    def drv_prod(expr):
        m1 = expr.get_mult1()
        m2 = expr.get_mult2()
        assert isinstance(m1, const)
        assert isinstance(m2, pwr)
        pr = drv.drv_pwr(m2)
        return maker.make_prod(maker.make_const(m1.get_val()*m2.get_deg().get_val()),pr)

    @staticmethod
    def drv_plus(expr):
        first = drv.drv(expr.get_elt1())
        second = drv.drv(expr.get_elt2())
        return maker.make_plus(first, second)
