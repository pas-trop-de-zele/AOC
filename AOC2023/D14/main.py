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

"""
The amount of load caused by a single rounded rock (O) is equal to the number of rows from the rock to the south edge of the platform, including the row the rock is on. (Cube-shaped rocks (#) don't contribute to load.) So, the amount of load caused by each rock in each row is as follows:
"""
M = list(fin)
for y in range(len(M)):
    M[y] = [c for c in M[y]]

def tilt(M, direction):
    H = len(M)
    W = len(M[0])
    if direction == 0: # NORTH
        for y in range(H):
            for x in range(W):
                done = False
                if M[y][x] == 'O':
                    M[y][x] = '.'
                    for yy in range(y-1, -1, -1):
                        if M[yy][x] in 'O#':
                            M[yy+1][x] = 'O'
                            done = True
                            break
                    if not done:
                        M[0][x] = 'O'   
    elif direction == 2: # SOUTH
        for y in range(H-1, -1, -1):
            for x in range(W):
                done = False
                if M[y][x] == 'O':
                    M[y][x] = '.'
                    for yy in range(y+1, H):
                        if M[yy][x] in 'O#':
                            M[yy-1][x] = 'O'
                            done = True
                            break
                    if not done:
                        M[H-1][x] = 'O'
    elif direction == 1: # EAST
        for x in range(W-1, -1, -1):
            for y in range(H):
                done = False
                if M[y][x] == 'O':
                    M[y][x] = '.'
                    for xx in range(x+1, W):
                        if M[y][xx] in 'O#':
                            M[y][xx-1] = 'O'
                            done = True
                            break
                    if not done:
                        M[y][W-1] = 'O'
    elif direction == 3: # WEST
        for x in range(W):
            for y in range(H):
                done = False
                if M[y][x] == 'O':
                    M[y][x] = '.'
                    for xx in range(x-1, -1, -1):
                        if M[y][xx] in 'O#':
                            M[y][xx+1] = 'O'
                            done = True
                            break
                    if not done:
                        M[y][0] = 'O'

def cycle():
    # debM(M)
    tilt(M, 0) # NORTH
    # debM(M)
    tilt(M, 3) # WEST
    # debM(M)
    tilt(M, 2) # SOUTH
    # debM(M)
    tilt(M, 1) # EAST 
    # debM(M)

def encode(M):
    locs = []
    for y in range(len(M)):
        for x in range(len(M[0])):
            if M[y][x] == 'O':
                locs.append((y,x))
    return tuple(sorted(locs))

lookup = {}
lookup[encode(M)] = -1
seen = set()
seen.add(encode(M))
N = 1000000000
div = 0
first = -1
for cycle_id in range(N):
    print(cycle_id + 1)
    cycle()
    hash_ = encode(M)
    if hash_ in seen:
        first = lookup[hash_]
        div = cycle_id - lookup[hash_]
        print('seen', cycle_id, lookup[hash_], div)
        break
    seen.add(hash_)
    lookup[hash_] = cycle_id

M = list(fin)
for y in range(len(M)):
    M[y] = [c for c in M[y]]

for _ in range(first):
    cycle()

N = (N - first) % div
for _ in range(N):
    cycle()

ret = 0
for y in range(len(M)):
    for x in range(len(M[0])):
        if M[y][x] == 'O':
            ret += len(M) - y
print(ret)