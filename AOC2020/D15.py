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
"""
If that was the first time the number has been spoken, the current player says 0.

Otherwise, the number had been spoken before; the current player announces how many turns apart the number is from when it was previously spoken.
"""
fin = sys.stdin.read().strip().split(',')
nums = [int(c) for c in fin]
lookup = {num : i for i,num in enumerate(nums)}
seen = set(nums)
last = 14
for i in range(6, 30000000):
    if last in seen:
        distance = i - 1 - lookup[last]
        lookup[last] = i - 1
        last = distance
    else:
        seen.add(last)
        lookup[last] = i - 1
        last = 0
    # print(nums)
print(last)