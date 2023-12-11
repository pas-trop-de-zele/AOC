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
def find_start():
    for y in range(H):
        for x in range(W):
            if M[y][x] == 'S':
                return (y, x)
q = deque()
Y, X = find_start()
seen = set([find_start()])
q.append((Y, X, 0))
seen.add((Y, X))
ret = 0
LEFT = '-FL'
RIGHT = '-7J'
UP = '|7F'
DOWN = '|LJ'
LOOP = [[], []]
while q:
    q_len = len(q)
    for loop_id in range(q_len):
        y, x, carry = q.popleft()
        ret = max(ret, carry)
        LOOP[loop_id].append((y, x))
        for dy, dx in MOVES_ADJACENT:
            yy = y + dy
            xx = x + dx
            if yy < 0 or yy >= H or xx < 0 or xx >= W or (yy, xx) in seen:
                continue
            
            me = M[y][x]
            they = M[yy][xx]
            if (me in 'S-' and dx==1 and they in RIGHT) or \
            (me in 'S-' and dx==-1 and they in LEFT) or \
            (me in 'S|' and dy==1 and they in DOWN) or \
            (me in 'S|' and dy==-1 and they in UP) or \
            (me in 'S7' and dy==1 and they in DOWN) or \
            (me in 'S7' and dx==-1 and they in LEFT) or \
            (me in 'SF' and dx==1 and they in RIGHT) or \
            (me in 'SF' and dy==1 and they in DOWN) or \
            (me in 'SJ' and dy==-1 and they in UP) or \
            (me in 'SJ' and dx==-1 and they in LEFT) or \
            (me in 'SL' and dx==1 and they in RIGHT) or \
            (me in 'SL' and dy==-1 and they in UP):
                q.append((yy, xx, carry+1))
                seen.add((yy,xx))

for x in LOOP[1][::-1]:
    LOOP[0].append((x))
LOOP[0].append((Y, X))
print(LOOP[0])
from matplotlib.path import Path
path = Path(LOOP[0])
inside = 0
for y in range(H):
    for x in range(W):
        if (y, x) not in seen and path.contains_point((y, x)):
            inside += 1
print(inside)