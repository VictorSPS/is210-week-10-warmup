#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Dictionary iteration"""


DATA = {
    1: 1100,
    2: 1122,
    3: 1133,
    4: 1144,
    5: 1155,
    6: 1166,
    7: 1177,
    8: 1188,
    9: 1199,
    10: 1200
}


def iter_dict_funky_sum(dict1):
    """Function takes one dictionary argument
    Arg:
       dict1(int): dictionary of integers.
    Return:
       returns the funky total.
    Examples:
       >>> iter_dict_funky_sum(DATA)
       11529
    """
    running_total = 0
    for key, values in dict1.iteritems():
        running_total += (values - key)
    return running_total
