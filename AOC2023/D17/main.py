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
M = [[int(c) for c in line] for line in fin]
H = len(M)
W = len(M[0])
class D(Enum):
    LEFT,RIGHT,UP,DOWN = 0,1,2,3
opp = {}
opp[D.LEFT] = D.RIGHT
opp[D.RIGHT] = D.LEFT
opp[D.UP] = D.DOWN
opp[D.DOWN] = D.UP
class State:
    def __init__(self, y, x, w, aim, straight):
        self.y = y
        self.x = x
        self.w = w
        self.aim = aim
        self.straight = straight
    def __lt__(self, o):
        return self.w < o.w

q = []
heapq.heappush(q, State(0,0, 0, D.DOWN, 1))
heapq.heappush(q, State(0,0, 0, D.RIGHT, 1))
seen = set()
# seen.append((0,0,D.DOWN,1))
# seen.append((0,0,D.RIGHT,1))
dist = defaultdict(lambda : math.inf)
dist[(0,0,D.DOWN,1)] = 0
dist[(0,0,D.RIGHT,1)] = 0
par = {}
while q:
    def bad(y,x):
        if y < 0 or y >= H or x < 0 or x >= W:
            return True
    def next_loc(aim):
        if aim == D.LEFT: return (y,x-1)
        elif aim == D.RIGHT: return (y,x+1)
        elif aim == D.UP: return (y-1, x)
        elif aim == D.DOWN: return (y+1, x)
    
    def get_delta(aim):
        if aim == D.LEFT: return (0,-1)
        elif aim == D.RIGHT: return (0,1)
        elif aim == D.UP: return (-1,0)
        elif aim == D.DOWN: return (1,0)
    
    state = heapq.heappop(q)
    y,x,w,aim,straight = state.y, state.x, state.w, state.aim, state.straight
    for next_aim in [D.LEFT, D.RIGHT, D.UP, D.DOWN]:
        if next_aim == opp[aim]: continue
        if next_aim == aim and straight == 10: continue
        if next_aim != aim:
            if straight < 4: continue
            dy,dx = get_delta(next_aim)
            end_y, end_x = y,x
            for _ in range(4):
                end_y += dy
                end_x += dx
            if bad(end_y, end_x):
                continue

        yy,xx = next_loc(next_aim)
        next_straight = straight + 1 if next_aim == aim else 1
        if not bad(yy,xx):
            new_dist = w + M[yy][xx]
            if new_dist < dist[(yy,xx,next_aim, next_straight)]:
                par[(yy,xx,next_aim, next_straight)] = (y,x,aim,straight)
                dist[(yy,xx,next_aim, next_straight)] = new_dist
                heapq.heappush(q, State(yy,xx, new_dist, next_aim, next_straight))
ret = math.inf
for k,v in dist.items():
    if k[0]==H-1 and k[1]==W-1:
        ret=min(ret, v)
print(ret)