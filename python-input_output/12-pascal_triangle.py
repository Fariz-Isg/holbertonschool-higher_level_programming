#!/usr/bin/python3
"""Module that defines a pascal_triangle function"""


def pascal_triangle(n):
    """Generate Pascal's triangle of n rows

    Args:
        n (int): Number of rows to generate

    Returns:
        list: List of lists representing Pascal's triangle, empty if n <= 0
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)

    return triangle
