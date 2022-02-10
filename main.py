#
# Author: Anthony Cella
# A program to be able to run numerical estimation functions
# such as euler's method, euler's improved, and rk4.
# Very useful to check your work in Differential Equations.
# Last updated: 2/9/2022
#


from result import *
import run


def function(x, y):

    function_result = 32 - ((0.125/8) * y * y)

    return function_result


def main():

    x0 = 0
    y0 = 0

    h = 0.01
    x_end = 5

    eulers_result_unrounded = get_eulers_estimation(x0, y0, x_end, h, function)
    eulers_result = round(eulers_result_unrounded, 4)
    print("Euler's Estimation:", eulers_result)

    improved_eulers_result_unrounded = get_improved_eulers_estimation(x0, y0, x_end, h, function)
    improved_eulers_result = round(improved_eulers_result_unrounded, 4)
    print("Improved Euler's Estimation Result:", improved_eulers_result)

    rk4_result_unrounded = get_rk4_estimation(x0, y0, x_end, h, function)
    rk4_result = round(rk4_result_unrounded, 4)
    print("RK4 Estimation Result:", rk4_result)

    run.run_eulers(function, x0, y0, h, x_end)
    run.run_improved_eulers(function, x0, y0, h, x_end)
    run.run_rk4(function, x0, y0, h, x_end)

main()
