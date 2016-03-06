__author__ = 'Michael'

import copy
from enum import Enum

# Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes,
# write a method to rotate the image by 90 degrees.
# Can you do this in place?

# Number of columns/rows
n = 3
matrix = [[0 for x in range(n)] for x in range(n)]
directions = Enum('Direction', 'clockwise widdershins')


def main():
    matrix[0][0] = 1
    matrix[0][1] = 2
    matrix[0][2] = 3
    matrix[1][0] = 4
    matrix[1][1] = 5
    matrix[1][2] = 6
    matrix[2][0] = 7
    matrix[2][1] = 8
    matrix[2][2] = 9

    print(matrix)
    print(rotate(matrix, directions.clockwise))
    print(rotate(matrix, directions.widdershins))


def rotate(the_matrix, direction):
    rotated = copy.deepcopy(the_matrix)

    for i in range(n):
        for j in range(n):
            if direction == directions.clockwise:
                rotated[j][n - (i + 1)] = the_matrix[i][j]
            elif direction == directions.widdershins:
                rotated[n - (j + 1)][i] = the_matrix[i][j]
    return rotated


if __name__ == '__main__':
    main()