#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):

    if len(matrix) == 1 and len(matrix[0]) == 0:
        print('')

    for row in matrix:
        for element in row:
            if element == row[-1]:
                print("{}".format(element))
                break
            print("{}".format(element), end=' ')
