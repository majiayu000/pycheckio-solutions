#!/usr/bin/env checkio --domain=py run triangular-islands

# The robots have discovered strange islands in the Bermuda Triangle.
# You have to help the robots calculate once again.
# 
# The triangular sea area is divided into a triangular area, numbered from top to bottom and from left to right.    (Row-major order)
# 
# You are given a set of integers with land numbers as input values.
# 
# Triangles with adjacent sides are considered to be a group of the same island.The number of those triangles is the area of the island.You have to return a list (or iterable) of the area of the island you found.
# 
# 
# END_DESC

from typing import Set, Iterable


def triangular_islands(triangles: Set[int]) -> Iterable[int]:

    # your code here
    return []


if __name__ == '__main__':
    print("Example:")
    print(sorted(triangular_islands({1})))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert sorted(triangular_islands({1})) == [1]
    assert sorted(triangular_islands({2, 3, 6})) == [3]
    assert sorted(triangular_islands({4, 3})) == [2]
    assert sorted(triangular_islands({1, 4, 7, 8})) == [1, 3]
    assert sorted(triangular_islands({1, 2, 3, 4, 5, 6, 7, 8, 9})) == [9]
    assert sorted(triangular_islands({1, 2, 4, 5, 7, 9})) == [1, 1, 1, 1, 1, 1]
    print("Coding complete? Click 'Check' to earn cool rewards!")