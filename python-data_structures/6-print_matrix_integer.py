#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    n = len(matrix[0])
    for i in range(n):
        if i == 0:
            pass
        else:
            print()
        for j in range(n):
            if j == n - 1:
                print("{:d}".format(matrix[i][j]), end="")
            else:
                print("{:d}".format(matrix[i][j]), end=" ")
    print()

