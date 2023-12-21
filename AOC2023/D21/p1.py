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
M = list(fin)
debM(M)
H = len(M)
W = len(M[0])

y,x = -1,-1
for r in range(H):
    done = False
    for c in range(W):
        if M[r][c] == 'S':
           y = r
           x = c
           done = True
           break 
    if done:
        break

def get_locs(q):
    ret = [(y,x) for y,x in q if y in range(H) and x in range(W)]
    return tuple(sorted(ret))

# N = 26501365
N = 64
q = deque([(y,x)])
cur = 0
prev = 0
first_side = set()
first_appear = defaultdict(list)
while True:
    q_len = len(q)
    for _ in range(q_len):
        y,x = q.popleft()
        for dy, dx in MOVES_ADJACENT:
            yy = y + dy
            xx = x + dx
            Y = yy
            X = xx
            if yy not in range(H):
                if yy >= H:
                    Y = yy % H
                elif yy < 0:
                    Y = (yy + H) % H
            if xx not in range(W):
                if xx >= W:
                    X = xx % W
                elif xx < 0:
                    X = (xx + W) % W
            val = M[Y][X]
            if val in 'S.':
                q.append((yy,xx))
    cur += 1
    q = set(q)
    q = deque(q)
    if cur == N:
        break