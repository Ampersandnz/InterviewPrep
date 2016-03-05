__author__ = 'Michael'

import copy

# Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0.

# Number of columns
m = 3
# Number of rows
n = 3
matrix = [[0 for x in range(m)] for x in range(n)]


def main():
    matrix[0][0] = 1
    matrix[0][1] = 2
    matrix[0][2] = 3
    matrix[1][0] = 4
    matrix[1][1] = 0
    matrix[1][2] = 6
    matrix[2][0] = 7
    matrix[2][1] = 8
    matrix[2][2] = 9

    print(matrix)
    print(zero(matrix))


def zero(the_matrix):
    zeroed = copy.deepcopy(the_matrix)

    for i in range(n):
        for j in range(m):
            if the_matrix[i][j] == 0:
                for x in range(n):
                    zeroed[x][j] = 0
                for y in range(m):
                    zeroed[i][y] = 0

    return zeroed


if __name__ == '__main__':
    main()