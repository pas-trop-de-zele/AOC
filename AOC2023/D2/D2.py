import sys
import math
from pprint import pprint as pprint
import heapq
from copy import *
from collections import *
import functools
from math import *

sys.setrecursionlimit(100000000)

def debM(m):
    for r in m:
        for c in r:
            print(c, end='')
        print()
    print()


MOVES_ADJACENT = [[1, 0], [0, 1], [-1, 0], [0, -1]]
MOVES_ALL = [[1, 0], [1, 1], [0, 1], [-1, 1],
             [-1, 0], [-1, -1], [0, -1], [1, -1]]

fin = sys.stdin.read().strip().split("\n")
ret = 0
for line in fin:
    game_id = int(line.split(":")[0].split(' ')[1])
    details = line[line.index(':')+1:]
    cube_sets = details.split(";")
    good = True
    mx_red = 0
    mx_blue = 0
    mx_green = 0
    for cube_set in cube_sets:
        red = 0
        blue = 0
        green = 0
        cubes = [x.strip() for x in cube_set.split(", ")]
        for cube in cubes:
            count, color = cube.split()
            count = int(count)
            if color == 'red':
                red += count
            elif color == 'blue':
                blue += count
            elif color == 'green':
                green += count
        mx_red = max(mx_red, red)
        mx_blue = max(mx_blue, blue)
        mx_green = max(mx_green, green)
    print(mx_red, mx_blue, mx_green)
    ret += mx_green * mx_blue * mx_red
print(ret)