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
Y = []
X = []
finite_points = []
points = []
for line in fin:
    x, y = [int(c) for c in line.split(',')]
    points.append((y, x))
    Y.append(y)
    X.append(x)

THRESHOLD = 10000
ret = 0
for y in range(min(Y), max(Y)+1):
    for x in range(min(X), max(X)+1):
        total_distance = 0
        for yy, xx in points:
            total_distance += abs(y-yy) + abs(x-xx)
        if total_distance < THRESHOLD:
            ret += 1
print(ret)