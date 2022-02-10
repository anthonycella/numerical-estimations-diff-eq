#
# Author: Anthony Cella
# A class containing methods to get estimations from
# euler's method, euler's improved, or rk4 without making
# a whole table from it. These are for folks who just want a straight
# answer in one number.
# Last updated: 2/9/2022
#

import eulers
import rk4


def get_eulers_estimation(x, y, x_end, h, function):
    if x == x_end:
        return y

    eulers_estimation = eulers.eulers_method(y, h, x, function)

    y = eulers_estimation
    x += h
    x = round(x, 4)

    return get_eulers_estimation(x, y, x_end, h, function)


def get_improved_eulers_estimation(x, y, x_end, h, function):
    if x == x_end:
        return y

    improved_eulers_estimation = eulers.improved_eulers_method(y, h, x, function)

    y = improved_eulers_estimation
    x += h
    x = round(x, 4)

    return get_improved_eulers_estimation(x, y, x_end, h, function)


def get_rk4_estimation(x, y, x_end, h, function):
    if x == x_end:
        return y

    rk4_estimation = rk4.get_rk4(function, x, y, h)

    y = rk4_estimation
    x += h
    x = round(x, 4)

    return get_rk4_estimation(x, y, x_end, h, function)
