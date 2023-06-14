#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return ([list(map(lambda a: a ** 2, b))for b in matrix])
