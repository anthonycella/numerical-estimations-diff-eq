#
# Author: Anthony Cella
# A class containing all of the helper methods
# for using rk4.
# Last updated: 2/9/2022
#

def get_all_values_for_row(function, xn, yn, h, n):
    k1 = get_k1(function, xn, yn)
    k2 = get_k2_or_k3(function, xn, yn, h, k1)
    k3 = get_k2_or_k3(function, xn, yn, h, k2)
    k4 = get_k4(function, xn, yn, h, k3)

    rk4 = get_rk4_value(yn, h, k1, k2, k3, k4)

    all_values = (n, xn, yn, k1, k2, k3, k4, rk4)
    return all_values


def get_rk4(function, xn, yn, h):
    k1 = get_k1(function, xn, yn)
    k2 = get_k2_or_k3(function, xn, yn, h, k1)
    k3 = get_k2_or_k3(function, xn, yn, h, k2)
    k4 = get_k4(function, xn, yn, h, k3)

    rk4 = get_rk4_value(yn, h, k1, k2, k3, k4)
    return rk4


def get_k1(function, xn, yn):
    k1 = function(xn, yn)
    return k1


def get_k2_or_k3(function, xn, yn, h, k1_or_k2):
    x_component = xn + (0.5 * h)
    y_component = yn + (0.5 * h * k1_or_k2)
    k2_or_k3 = function(x_component, y_component)

    return k2_or_k3


def get_k4(function, xn, yn, h, k3):
    x_component = xn + h
    y_component = yn + (h * k3)
    k4 = function(x_component, y_component)

    return k4


def get_rk4_value(yn, h, k1, k2, k3, k4):
    h_component = (h/6) * (k1 + (2*k2) + (2*k3) + k4)
    rk4_value = yn + h_component

    return rk4_value


