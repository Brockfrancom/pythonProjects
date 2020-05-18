####################################
# module: rxp.py
# Brock Francom
# A02052161
####################################

import numpy as np

class rxp(object):

    @staticmethod
    def drv1(f, cdd, x, h):
        return cdd(f, x, h)

    @staticmethod
    def drv2(f, cdd, x, h):
        x1 = rxp.drv1(f, cdd, x, h/2.0)
        x2 = rxp.drv1(f, cdd, x, h)
        return  np.longdouble(x1 + (x1 - x2)/3.0)

    @staticmethod
    def drv3(f, cdd, x, h):
        x1 = rxp.drv2(f, cdd, x, h/2.0)
        x2 = rxp.drv2(f, cdd, x, h)
        return  np.longdouble(x1 + (x1 - x2)/15.0)

    @staticmethod
    def drv4(f, cdd, x, h):
        x1 = rxp.drv3(f, cdd, x, h/2.0)
        x2 = rxp.drv3(f, cdd, x, h)
        return  np.longdouble(x1 + (x1 - x2)/63.0)
