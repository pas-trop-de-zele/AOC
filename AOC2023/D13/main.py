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

def is_col_reflected(col, M):
    # col always on the right
    # col has to be >= 1
    H = len(M)
    W = len(M[0])
    good = True
    for y in range(H):
        left, right = col-1, col
        while left >= 0 and right < W:
            if M[y][left] != M[y][right]:
                good = False
            left -= 1
            right += 1
    return good

def is_row_reflected(row, M):
    # row always under 
    H = len(M)
    W = len(M[0])
    good = True
    for x in range(W):
        up, down = row-1, row
        while up >= 0 and down < H:
            if M[up][x] != M[down][x]:
                good = False
            up -= 1
            down += 1
    return good

def get_cols(M):
    W = len(M[0])
    ret = []
    for col in range(1, W):
        if is_col_reflected(col, M):
            ret.append(col)
    return sorted(tuple(ret))

def get_rows(M):
    H = len(M)
    ret = []
    for row in range(1, H):
        if is_row_reflected(row, M):
            ret.append(row)
    return sorted(tuple(ret))

def calc(M):
    H = len(M)
    W = len(M[0])
    row_done = set()
    col_done = set()
    legacy_row_gain = get_rows(M)
    legacy_col_gain = get_cols(M)
    for y in range(H):
        for x in range(W):
            newM = list(M)
            new_row = [c for c in M[y]]
            new_row[x] = '.' if new_row[x] == '#' else '#'
            newM[y] = new_row
            row_gain = get_rows(newM)
            col_gain = get_cols(newM)
            if legacy_row_gain != row_gain or legacy_col_gain != col_gain:
                row_add = [c for c in row_gain if c not in legacy_row_gain and c not in row_done]
                col_add = [c for c in col_gain if c not in legacy_col_gain and c not in col_done]
                row_done.update(set(row_add))
                col_done.update(set(col_add))
                global ROWS, COLS
                ROWS += sum(row_add)
                COLS += sum(col_add)
                print(row_add, col_add)

fin = sys.stdin.read().strip().split("\n\n")
patterns = fin
ROWS = 0
COLS = 0
for id_, pattern in enumerate(patterns):
    M = pattern.split('\n')
    calc(M)
    print('=' * 20)
print(ROWS, COLS)
print(100*ROWS + COLS)