import sys
from math import *
from pprint import pprint as pprint
import heapq
from copy import *
from collections import *
import functools
from itertools import *

# sys.setrecursionlimit(100000000)

class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size
        self.components = size
        
    def find(self, x):
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        if not self.is_connected(x, y):
            rootX = self.root[x]
            rootY = self.root[y]
            if self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            elif self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1
            self.components -= 1

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)

    def distinct_components(self):
        return self.components

def debM(m):
    for r in m:
        for c in r:
            print(c, end='')
        print()
    print()


def is_same(lookup):
    times = set()
    for start in lookup.values():
        times.add(start)
    return len(times) == 1 

MOVES_ADJACENT = [[1, 0], [0, 1], [-1, 0], [0, -1]]
MOVES_ALL = [[1, 0], [1, 1], [0, 1], [-1, 1],
             [-1, 0], [-1, -1], [0, -1], [1, -1]]
fin = sys.stdin.read().strip().split("\n")
lookup = Counter()
cur_direction = 'E'
all_directions = 'NESW'
pointer = 1
for l in fin:
    direction, distance = l[:1], l[1:]
    distance = int(distance)
    print(direction, distance, cur_direction)
    if direction == 'F':
        lookup[cur_direction] += distance
    elif direction in 'NESW':
        lookup[direction] += distance
    else:
        turns = distance // 90 % 4
        if direction == 'R':
            pointer = (pointer + turns) % 4
        elif direction == 'L':
            pointer = (pointer + (4 - turns)) % 4
        cur_direction = all_directions[pointer]
    print(lookup)
print(abs(lookup['N'] - lookup['S']) + abs(lookup['E'] - lookup['W']))