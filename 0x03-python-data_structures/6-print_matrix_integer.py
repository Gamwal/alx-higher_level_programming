#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for pos, j in enumerate(i):
            print("{:d}".format(j),end='')
            if pos != len(i)-1:
                print(" ", end='')
        print("")
