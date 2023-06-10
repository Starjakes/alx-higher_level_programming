#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    l = len(matrix)
    for m in range(l):
        for m2 in range(len(matrix[m])):
            print('{:d}'.format(matrix[m][m2]), end='')
            if m2 is not (len(matrix[m]) - 1):
                print(end=" ")
        print("")
