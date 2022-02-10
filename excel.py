#
# Author: Anthony Cella
# A class that handles the tables made in the table.py class
# and puts them into a .csv file that can be read by Microsoft Excel
# Last updated: 2/9/2022
#


def create_csv(table_rows, file_name, first_row_values):
    csv_file = open(file_name, "w")
    write_first_row(csv_file, first_row_values)

    for row in table_rows:
        write_row(csv_file, row)

    csv_file.close()


def write_row(csv_file, row):
    csv_file.write(row + '\n')


def write_first_row(csv_file, first_row_values):
    csv_file.write(first_row_values + "\n")


def clear_line(csv_file):
    csv_file.write(",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,")


def clear_table(csv_file, number_of_rows):
    for number in range(0, number_of_rows):
        clear_line(csv_file)

