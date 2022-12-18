import sys
from math import *
from pprint import pprint as pprint
from sympy.ntheory.modular import crt
import heapq
from copy import *
from collections import *
import functools
from itertools import *
from math import sqrt, ceil
import threading
import cmath  
import itertools
# sys.setrecursionlimit(100000000)

maxx = maxy = maxz = -inf
def is_touched(a, b):
    return (abs(a[0] - b[0]) + abs(a[1] - b[1]) + abs(a[2] - b[2])) == 1

def count_exposed(a):
    ret = 0
    for b in cubes:
        if is_touched(a, b):
            ret += 1
    return 6 - ret

fin = sys.stdin.read().strip().split("\n")
cubes = set()
for l in fin:
    x, y, z = map(int, l.split(","))
    maxx = max(maxx, x)
    maxy = max(maxy, y)
    maxz = max(maxz, z)
    cubes.add((x, y, z))


def count_all_exposed():
    ret = 0
    for a in cubes:
        ret += count_exposed(a)
    return ret

SURROUND = [
    (0,1,0),
    (1,0,0),
    (0,-1,0),
    (-1,0,0),
    (0,0,1),
    (0,0,-1),
]

seen = set()

water_touches=0
def get_air_pocket_area(x, y, z):
    is_enclosed = True
    touched = 0
    q = deque([(x, y, z)])
    seen.add((x, y, z))
    while q:
        cube = q.pop()
        x, y, z = cube
        for dx, dy, dz in SURROUND:
            xx = x + dx
            yy = y + dy
            zz = z + dz

            if not -1 <= xx <= maxx + 1 or \
                not -1 <= yy <= maxy + 1 or \
                not -1 <= zz <= maxz + 1 or \
                (xx,yy,zz) in seen:
                continue

            # Touch cubes
            if (xx,yy,zz) in cubes:
                touched += 1
                continue

            # Since these cells are non cubes, if they are at the edges
            # # means that water can touch them
            if 0 in (xx, yy, zz) or \
                xx == maxx or \
                yy == maxy or \
                zz == maxz:
                is_enclosed = False

            seen.add((xx, yy, zz))
            q.append((xx, yy, zz))
    
    if not is_enclosed:
        global water_touches
        water_touches += touched
    return touched if is_enclosed else 0

def count_inner_sides():
    ret = 0
    for x in range(-1,maxx + 2):
        for y in range(-1,maxy + 2):
            for z in range(-1,maxz + 2):
                # Only check unseen blocks that are non cubes
                if (x, y, z) in seen or (x, y, z) in cubes:
                    continue
                ret += get_air_pocket_area(x, y, z)
    return ret

def p2():
    all_areas = count_all_exposed()
    inner_sides = count_inner_sides()
    print("ALL AREAS", all_areas)
    print("ENCLOSED", inner_sides)
    print("INNER", all_areas - inner_sides)
    # This is a test to make sure the bfs is working correctly
    print("WATER TOUCHED", water_touches)
p2()