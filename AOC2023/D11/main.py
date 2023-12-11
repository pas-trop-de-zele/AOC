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
M = fin
H = len(M)
W = len(M[0])
galaxies = []
for y in range(H):
    for x in range(W):
        if M[y][x] == '#':
            galaxies.append((y, x))

def is_row_empty(row):
    return all(M[row][col] == '.' for col in range(W))

def is_col_empty(col):
    return all(M[row][col] == '.' for row in range(H))

ROW_PREFIX = [is_row_empty(row) for row in range(H)]
for row in range(1, H): ROW_PREFIX[row] += ROW_PREFIX[row-1]

COL_PREFIX = [is_col_empty(col) for col in range(W)]
for col in range(1, W): COL_PREFIX[col] += COL_PREFIX[col-1]

ADD = 999999
ret = 0
for i in range(len(galaxies)):
    for j in range(i+1, len(galaxies)):
        a = galaxies[i]
        b = galaxies[j]
        gain = abs(a[0]-b[0]) + abs(a[1]-b[1])

        if a[0] < b[0]:
            gain += (ROW_PREFIX[b[0]] - ROW_PREFIX[a[0]]) * ADD
        else:
            gain += (ROW_PREFIX[a[0]] - ROW_PREFIX[b[0]]) * ADD
        if a[1] < b[1]:
            gain += (COL_PREFIX[b[1]] - COL_PREFIX[a[1]]) * ADD
        else:
            gain += (COL_PREFIX[a[1]] - COL_PREFIX[b[1]]) * ADD
        ret += gain
print(ret)
                