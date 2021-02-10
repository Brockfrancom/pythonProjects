####################################
# module: cdd.py
# Brock Francom
# A02052161
####################################

import numpy as np

class cdd(object):

    @staticmethod
    def drv1_ord2(f, x, h):
        ### Table 6.3 formula 1, p. 339 in CDD handout
        return np.longdouble((f(x+h) - f(x-h))/(2*h))

    @staticmethod
    def drv1_ord4(f, x, h):
        ### Table 6.4 formula 1, p. 339 in the CDD handout
        return np.longdouble((-1*f(x+2*h) +8*f(x+h) - 8*f(x-h) + f(x-2*h))/(12*h))

    @staticmethod
    def drv2_ord2(f, x, h):
        ### Table 6.3, formula 2, p. 339 in CDD handout
        f0 = cdd.drv1_ord2(f, x, h)
        return np.longdouble((f(x+h) -2*f(x) + f(x-h))/(h*h))

    @staticmethod
    def drv2_ord4(f, x, h):
        ### Table 6.4, formula 2, p. 339 in CDD handout
        return np.longdouble((-1*f(x+2*h) + 16*f(x+h) - 30*f(x) + 16*f(x-h) - f(x-2*h))/(12*h*h))
