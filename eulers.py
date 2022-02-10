#
# Author: Anthony Cella
# A class containing all of the helper methods for implementing
# both euler's method and euler's improved.
# Last updated: 2/9/2022
#

def eulers_method(yn, h, xn, function):
    yn_plus_one = yn + (h * function(xn, yn))
    return yn_plus_one


def improved_eulers_method(yn, h, xn, function):
    xn_plus_one = xn + h
    yn_plus_one_star = eulers_method(yn, h, xn, function)

    one_half_h = h / 2
    added_functions = function(xn, yn) + function(xn_plus_one, yn_plus_one_star)

    yn_plus_one = yn + (one_half_h * added_functions)
    return yn_plus_one


def get_all_values_for_row(function, xn, yn, h, n):
    eulers_output = eulers_method(yn, h, xn, function)
    all_values = [n, xn, yn, eulers_output]
    return all_values


def get_all_values_for_row_improved(function, xn, yn, h, n):
    all_values = get_all_values_for_row(function, xn, yn, h, n)
    improved_eulers_output = improved_eulers_method(yn, h, xn, function)
    all_values.append(improved_eulers_output)
    return all_values
