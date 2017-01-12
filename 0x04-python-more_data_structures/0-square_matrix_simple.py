#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for line in matrix:
        new_list = []
        for i in line:
            new_list.append(i * i)
        new_matrix.append(new_list)
    return (new_matrix)
