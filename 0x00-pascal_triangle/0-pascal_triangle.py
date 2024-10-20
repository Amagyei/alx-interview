#!/usr/bin/python3
"""
Pascal's Triangle
"""


def create_list(i):
    '''Returns a list of 1s'''
    return [1] * (i + 1)


def triangle_populator(triangle):
    '''Populates each list of the triangle with correct value'''
    triangle[0][0] = 1
    for i in range(1, len(triangle)):
        for j in range(1, len(triangle[i]) - 1):
            if j >= len(triangle[j]):
                continue
            triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
    return triangle


def pascal_triangle(n):
    ''' Makes the triangle'''
    triangle = []
    if n <= 0:
        return triangle
    for i in range(n):
        triangle.append(create_list(i))
    return triangle_populator(triangle)
