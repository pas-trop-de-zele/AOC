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
class D(Enum):
    LEFT,RIGHT,UP,DOWN = 0,1,2,3

M = list(fin)
H = len(M)
W = len(M[0])

def f(q, seen):
    while q:
        def bad(d, y, x):
            return y < 0 or y >= H or x < 0 or x >= W or (d,y,x) in seen
        def left():
            if not bad(D.LEFT,y,x-1):
                q.append((D.LEFT,y,x-1))
                seen.add((D.LEFT,y,x-1))
        def right():
            if not bad(D.RIGHT,y,x+1):
                q.append((D.RIGHT,y,x+1))
                seen.add((D.RIGHT,y,x+1))
        def up():
            if not bad(D.UP,y-1,x):
                q.append((D.UP,y-1,x))
                seen.add((D.UP,y-1,x))
        def down():
            if not bad(D.DOWN,y+1,x):
                q.append((D.DOWN,y+1,x))
                seen.add((D.DOWN,y+1,x))

        d,y,x = q.popleft()
        val = M[y][x]

        if val == '.':
            for dy, dx in MOVES_ADJACENT:
                if d == D.LEFT and dx == -1: left()
                elif d == D.RIGHT and dx == 1: right()
                elif d == D.UP and dy == -1: up()
                elif d == D.DOWN and dy == 1: down()
        elif val == '/':
            if d == D.LEFT: down()
            elif d == D.RIGHT: up()
            elif d == D.UP: right()
            elif d == D.DOWN: left()
        elif val == '\\':
            if d == D.LEFT: up()
            elif d == D.RIGHT: down()
            elif d == D.UP: left()
            elif d == D.DOWN: right()
        elif val == '-':
            if d == D.LEFT: left()
            elif d == D.RIGHT: right()
            elif d in (D.UP, D.DOWN): left(), right()
        elif val == '|':
            if d in (D.LEFT, D.RIGHT): up(), down()
            elif d == D.UP: up()
            elif d == D.DOWN: down()
    return len(set([(y,x) for _,y,x in seen]))

ret = 0
for y in range(1,H-1):
    state = [(D.RIGHT,y,0)]
    ret = max(ret, f(deque(state), set(state)))
    state = [(D.LEFT,y,W-1)]
    ret = max(ret, f(deque(state), set(state)))
for x in range(1,W-1):
    state = [(D.DOWN,0,x)]
    ret = max(ret, f(deque(state), set(state)))
    state = [(D.UP,H-1,x)]
    ret = max(ret, f(deque(state), set(state)))
# upper left corner
state = [(D.RIGHT,0,0), (D.DOWN,0,0)]
ret = max(ret, f(deque(state), set(state)))
# upper right corner
state = [(D.LEFT,0,W-1), (D.DOWN,0,W-1)]
ret = max(ret, f(deque(state), set(state)))
# lower left corner
state = [(D.UP,H-1,0), (D.RIGHT,H-1,0)]
ret = max(ret, f(deque(state), set(state)))
# lower right corner
state = [(D.UP,H-1,W-1), (D.LEFT,H-1,W-1)]
ret = max(ret, f(deque(state), set(state)))
print(ret)

