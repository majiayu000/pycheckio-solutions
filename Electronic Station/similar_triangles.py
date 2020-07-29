#!/usr/bin/env checkio --domain=py run similar-triangles

# This is a mission to check thesimilarityof two triangles.
# 
# You are given two lists as coordinates of vertices of each triangle.
# You have to return a bool. (The triangles are similar or not)
# 
# 
# END_DESC

from typing import List, Tuple
from math import sqrt
Coords = List[Tuple[int, int]]


def similar_triangles(coords_1: Coords, coords_2: Coords) -> bool:

    # your code here
    l = 3
    s = []
    k = []
    for i in range(3):
        if i <2:
           c =  (coords_1[i+1][0]-coords_1[i][0])**2 + (coords_1[i+1][1] - coords_1[i][1])**2
        else :
           c =  (coords_1[2][0] - coords_1[0][0])**2 + (coords_1[2][1] - coords_1[0][1])**2
               
        s.append(c)
           
    for i in range(3):
        if i <2:
           c =  (coords_2[i+1][0]-coords_2[i][0])**2 + (coords_2[i+1][1] - coords_2[i][1])**2
        else :
           c =  (coords_2[2][0] - coords_2[0][0])**2 + (coords_2[2][1] - coords_2[0][1])**2
               
        k.append(c)
    s.sort()
    k.sort()
    if s[0]/k[0] == s[1]/k[1] and s[1]/k[1] == s[2] / k[2] and s[2]/ k[2] == s[0] / k[0]:
        return True
    
    return False


if __name__ == '__main__':
    print("Example:")
    print(similar_triangles([(1, 0), (3, 3), (3, -2)], [(4, 3), (10, 9), (10, -6)]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 2), (5, 0)]) is True, 'basic'
    assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 3), (5, 0)]) is False, 'different #1'
    assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(2, 0), (4, 4), (6, 0)]) is True, 'scaling'
    assert similar_triangles([(0, 0), (0, 3), (2, 0)], [(3, 0), (5, 3), (5, 0)]) is True, 'reflection'
    assert similar_triangles([(1, 0), (1, 2), (2, 0)], [(3, 0), (5, 4), (5, 0)]) is True, 'scaling and reflection'
    assert similar_triangles([(1, 0), (1, 3), (2, 0)], [(3, 0), (5, 5), (5, 0)]) is False, 'different #2'
    print("Coding complete? Click 'Check' to earn cool rewards!")