#
# Author: Anthony Cella
# A class containing functions that create an array of values from
# the results of its method (rk4, euler's, and euler's improved).
# These values are in the format that can be written to a .csv file.
# Last updated: 2/9/2022
#

import eulers
import rk4


def construct_table_rk4(function, x0, y0, h, number_of_steps):
    rows = []

    n = 0
    second_row_values = rk4.get_all_values_for_row(function, x0, y0, h, n)
    second_row = values_to_csv_row_rk4(second_row_values) + ",," + str(h)
    rows.append(second_row)

    previous_rk4 = second_row_values[7]

    for step in range(0, number_of_steps):
        n += 1
        xn = x0 + (n*h)
        yn = previous_rk4

        row_values = rk4.get_all_values_for_row(function, xn, yn, h, n)
        new_row = values_to_csv_row_rk4(row_values)
        rows.append(new_row)

        previous_rk4 = row_values[7]

    return rows


def construct_table_eulers(function, x0, y0, h, number_of_steps):
    rows = []

    n = 0
    second_row_values = eulers.get_all_values_for_row(function, x0, y0, h, n)
    second_row = values_to_csv_row_eulers(second_row_values) + ",," + str(h)
    rows.append(second_row)

    previous_eulers = second_row_values[3]

    for step in range(0, number_of_steps):
        n += 1
        xn = x0 + (n*h)
        yn = previous_eulers

        row_values = eulers.get_all_values_for_row(function, xn, yn, h, n)
        new_row = values_to_csv_row_eulers(row_values)
        rows.append(new_row)

        previous_eulers = row_values[3]

    return rows


def construct_table_improved_eulers(function, x0, y0, h, number_of_steps):
    rows = []

    n = 0
    second_row_values = eulers.get_all_values_for_row_improved(function, x0, y0, h, n)
    second_row = values_to_csv_row_improved_eulers(second_row_values) + ",," + str(h)
    rows.append(second_row)

    previous_eulers_improved = second_row_values[4]

    for step in range(0, number_of_steps):
        n += 1
        xn = x0 + (n*h)
        yn = previous_eulers_improved

        row_values = eulers.get_all_values_for_row_improved(function, xn, yn, h, n)
        new_row = values_to_csv_row_improved_eulers(row_values)
        rows.append(new_row)

        previous_eulers_improved = row_values[4]

    return rows


def values_to_csv_row_rk4(values):
    output_string = str(values[0]) + ",," + str(values[1]) + ',' \
        + str(values[2]) + ',' + str(values[3]) + ',' + str(values[4]) + ',' \
        + str(values[5]) + ',' + str(values[6]) + ',,' + str(values[7])

    return output_string


def values_to_csv_row_eulers(values):
    output_string = str(values[0]) + ",, " + str(values[1]) + ',' \
        + str(values[2]) + ",," + str(values[3])

    return output_string


def values_to_csv_row_improved_eulers(values):
    output_string = values_to_csv_row_eulers(values) + ",," + str(values[4])
    return output_string
