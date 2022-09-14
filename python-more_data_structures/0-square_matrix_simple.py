#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_list = []
    new_list = [[dat ** 2 for dat in matrix[i]] for i in range(len(matrix))]
    return new_list
