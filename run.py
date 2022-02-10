#
# Author: Anthony Cella
# A class containing three "run" functions that output the results of a particular estimation
# (rk4, euler's method, or euler's improved) in a .csv file. The last function, get_number_of_steps(),
# is a helper function which is in each of the run methods and helps get the number of additional rows
# a table will need,
# Last updated: 2/9/2022
#

from excel import create_csv
from table import construct_table_improved_eulers, construct_table_eulers, construct_table_rk4


def get_number_of_steps(x0, x_end, h):
    # helps get the number of additional rows a table will need
    interval = x_end - x0
    number_of_steps = interval / h
    return number_of_steps


def run_rk4(function, x0, y0, h, x_end):
    number_of_steps = get_number_of_steps(x0, x_end, h)

    file_name = "rk4.csv"
    first_row_values = "n,,x,y,k1,k2,k3,k4,,rk4 output,,h number"
    table = construct_table_rk4(function, x0, y0, h, number_of_steps)

    create_csv(table, file_name, first_row_values)

    print("RK4 Excel Table Created Successfully")


def run_eulers(function, x0, y0, h, x_end):
    number_of_steps = get_number_of_steps(x0, x_end, h)

    file_name = "eulers.csv"
    first_row_values = "n,,x,y,,euler's output,,h number"
    table = construct_table_eulers(function, x0, y0, h, number_of_steps)

    create_csv(table, file_name, first_row_values)

    print("Euler's Excel Table Created Successfully")


def run_improved_eulers(function, x0, y0, h, x_end):
    number_of_steps = get_number_of_steps(x0, x_end, h)

    file_name = "eulers_improved.csv"
    first_row_values = "n,,x,y,,euler's output,,improved euler's output,,h number"
    table = construct_table_improved_eulers(function, x0, y0, h, number_of_steps)

    create_csv(table, file_name, first_row_values)

    print("Euler's Improved Excel Table Created Successfully")
