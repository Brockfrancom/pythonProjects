#!/usr/bin/python

#################################################
# module: parser.py
# YOUR NAME
# YOUR A#
#################################################

from maker import maker

class parser(object):

    @staticmethod
    def parse_elt(elt):
        # let's make sure that elt is a string.
        assert isinstance(elt, str)
        elt = elt.split('^')
        prod = maker.make_prod(maker.make_const(float(elt[0][:-1])), maker.make_pwr(elt[0][-1], float(elt[1])))
        return prod

    @staticmethod
    def parse_sum(poly_str):
        assert isinstance(poly_str, str)
        poly_str = poly_str.split(' ')
        ele = poly_str.pop(0)
        poly_sum = parser.parse_elt(ele)
        while(True):
            try:
                operand = poly_str.pop(0)
                element = poly_str.pop(0)
            except Exception:
                break
            if operand == '+':
                poly_sum = maker.make_plus(poly_sum, parser.parse_elt(element))
            else:
                poly_sum = maker.make_plus(poly_sum, parser.parse_elt(operand+element))
        return poly_sum
