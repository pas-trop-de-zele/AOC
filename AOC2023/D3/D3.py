import sys
import math
from pprint import pprint as pprint
import heapq
from copy import *
from collections import *
import functools
from math import *
from dataclasses import dataclass
from icecream import ic

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

class State:
    def __init__(self, y, x, dist):
        self.y = y
        self.x = x
        self.dist = dist
    
    def __lt__(self, o):
        return self.dist < o.dist
    
states = [State(1,0,1), State(1,1,2), State(0,0,10)]
q = []
for s in states:
    heapq.heappush(q, s)

while q:
    state = heapq.heappop(q)
    print(state.y, state.x, state.dist)