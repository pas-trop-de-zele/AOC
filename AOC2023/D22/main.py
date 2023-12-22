import sys
import math
from pprint import pprint as pprint
import heapq
from copy import *
from collections import *
import functools
from math import *
from dataclasses import dataclass
from hashlib import md5
from itertools import permutations
from sympy.ntheory.modular import crt 
import hashlib
from time import sleep
from enum import Enum
import json
import copy

sys.setrecursionlimit(10000000)

def debM(m):
    for r in m:
        for c in r:
            print(c, end='')
        print()
    print()


MOVES_ADJACENT = [[1, 0], [0, 1], [-1, 0], [0, -1]]
MOVES_ALL = [[1, 0], [1, 1], [0, 1], [-1, 1],
             [-1, 0], [-1, -1], [0, -1], [1, -1]]


fin = sys.stdin.read().strip().split('\n')
CUBES = []
MAX_HEIGHT = 0
for line in fin:
    left, right = line.split('~')
    left = [int(c) for c in left.split(',')]
    right = [int(c) for c in right.split(',')]
    CUBES.append([[left[0], right[0]], [left[1], right[1]],[left[2], right[2]]])
    MAX_HEIGHT = max(MAX_HEIGHT, right[2])


def share_space(cubes, u, v):
    A = cubes[u]
    B = cubes[v]
    X,Y,_ = A
    x1,x2 = X
    y1,y2 = Y

    XX,YY,_ = B
    xx1,xx2 = XX
    yy1,yy2 = YY

    Aspots = set()
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            Aspots.add((x,y))

    Bspots = set()
    for x in range(xx1, xx2+1):
        for y in range(yy1, yy2+1):
            Bspots.add((x,y))

    if Aspots & Bspots:
        return True
    return False

def count_support(cubes, my_cube_id):
    ret = 0
    A = cubes[my_cube_id]
    Alo = A[2][0]
    for other_cube_id in range(len(cubes)):
        if my_cube_id != other_cube_id:
            B = cubes[other_cube_id]
            Bhi = B[2][1]
            if Alo - 1 == Bhi and share_space(cubes, my_cube_id, other_cube_id):
                ret += 1
    return ret

def fall(cubes, cube_id):
    # simulate cube falling
    A = cubes[cube_id]
    z1,z2 = A[2]
    changed = False
    while z1 > 1:
        # before failling to next level check to make sure we wont touch any thing
        stop = False

        for i in range(len(cubes)):
            other_cube_hi_point = cubes[i][2][1]
            if cube_id != i and other_cube_hi_point == z1-1 and share_space(cubes, cube_id, i):
                stop = True

        if stop:
            break

        # move the cube down by 1
        z1 -= 1
        z2 -= 1
        changed = True
    A[2] = [z1, z2]
    cubes[cube_id] = A
    return changed

def get_stabilize_config(cubes):
    ret = copy.deepcopy(cubes)
    ret.sort(key=lambda cube : cube[2])
    # Simulate fall
    fall_times = 0
    cube_id_changed = set()
    while True:
        changed = False
        for cube_id in range(len(ret)):
            if fall(ret, cube_id):
                cube_id_changed.add(cube_id)
                changed = True
        fall_times += 1
        if not changed:
            break
    return (ret, len(cube_id_changed))


"""
overcomplicated it, already have fall() function, just have to rewrote to be able to fall from the parameter config
"""

def p1():
    global CUBES
    cubes,_ = get_stabilize_config(CUBES)
    ret = 0
    for cube_id in range(len(cubes)):
        A = cubes[cube_id]
        Ahi = A[2][1]
        bad = False
        
        # Check to see if supporting any other cubes
        for other_cube_id in range(len(cubes)):
            if cube_id != other_cube_id:
                B = cubes[other_cube_id]
                Blo = B[2][0]

                # check to see if there are any other cube that is being supported by this one
                if Ahi + 1 == Blo and share_space(cubes, cube_id, other_cube_id):

                    if count_support(cubes, other_cube_id) == 1:
                        bad = True
                
        if not bad:
            ret += 1
    print(ret)

def p2():
    global CUBES
    CUBES, _ = get_stabilize_config(CUBES)
    ret = 0
    for NODE in range(len(CUBES)):
        cubes = [x for i,x in enumerate(CUBES) if i != NODE]
        _, changed_count = get_stabilize_config(cubes)
        ret += changed_count
    print(ret)

if __name__=="__main__":
    p1()
    p2()