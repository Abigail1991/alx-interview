#!/usr/bin/python3
"""
Island Perimeter module
"""


def island_perimeter(grid):
    """Returns the perimeter of the island described in grid"""
    perimeter = 0
    grid_length = len(grid) - 1
    grid_width = len(grid[0]) - 1

    for i, r in enumerate(grid):
        for j, n in enumerate(r):
            if n == 1:
                if i == 0 or grid[i - 1][j] != 1:
                    perimeter += 1
                if j == 0 or grid[i][j - 1] != 1:
                    perimeter += 1
                if j == grid_width or grid[i][j + 1] != 1:
                    perimeter += 1
                if i == grid_length or grid[i + 1][j] != 1:
                    perimeter += 1
    return perimeter
