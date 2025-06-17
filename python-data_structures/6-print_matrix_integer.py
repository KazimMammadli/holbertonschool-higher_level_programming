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
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_matrix_integer(matrix)
print("--")
print_matrix_integer()
