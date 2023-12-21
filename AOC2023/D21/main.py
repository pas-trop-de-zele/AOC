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
H = len(M)
W = len(M[0])

def find_start(M):
    for r in range(H):
        for c in range(W):
            if M[r][c] == 'S':
                return (r,c)
y,x = find_start(M)

def get_locs(q):
    ret = [(y,x) for y,x in q if y in range(H) and x in range(W)]
    return tuple(sorted(ret))

H_MAX = -math.inf
H_MIN = math.inf
W_MAX = -math.inf
W_MIN = math.inf

def update_dimension(Y,X):
    H_MAX = max(H_MAX, Y)
    H_MIN = min(H_MIN, Y)
    W_MAX = max(W_MAX, X)
    W_MIN = min(W_MIN, X)

# N = 26501365
N = 500
q = deque([(y,x)])
cur = 0
prev = 0
side = set()

# (side_y, side_x) is a key
is_stable = {}
odd = {}
even = {}

# (side_y, side_x, M encode) is key
# if there are 2 encode appear twice -> assuming good? not sure if other state would be the same
side_config_counter = Counter() 

first_appear = defaultdict(list)

for N in [65, 196, 327, 458]:
    while True:
        q_len = len(q)
        for _ in range(q_len):
            y,x = q.popleft()
            for dy, dx in MOVES_ADJACENT:
                yy = y + dy
                xx = x + dx
                if M[yy%H][xx%W] in 'S.':
                    q.append((yy,xx))
        cur += 1
        q = set(q)
        encode = get_locs(q)
        first_appear[encode].append(cur)
        q = deque(q)
        if cur == N:
            print(cur, len(q))
            break
    
# 65, 196, 327