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
Immediately before a value is written to memory, each bit in the bitmask modifies the corresponding bit of the destination memory address in the following way:
If the bitmask bit is 0, the corresponding memory address bit is unchanged.
If the bitmask bit is 1, the corresponding memory address bit is overwritten with 1.
If the bitmask bit is X, the corresponding memory address bit is floating.
"""
def get_mem(s):
    open_brace = s.find('[')
    closing_brace = s.find(']')
    return int(s[open_brace + 1:closing_brace])

fin = sys.stdin.read().strip().split("\n")
mask = ''
lookup = {}
for l in fin:
    if l[0:4] == 'mask':
        mask = l.split()[2]
    else:
        mem = get_mem(l)
        mem_bit = bin(mem)[2:].rjust(36, '0')
        masked_mem = ''
        for vv, mm in zip(mem_bit, mask):
            if mm == '0':
                masked_mem += vv
            else:
                masked_mem += mm
        print(mem)
        print(masked_mem)
        all_mems = []
        floating_indices = [i for i, bit in enumerate(masked_mem) if bit == 'X']        
        for i in range(0, 2 ** len(floating_indices)):
            perm = bin(i)[2:].rjust(len(floating_indices), '0')
            new_mem = [c for c in masked_mem]
            for i in range(len(perm)):
                new_mem[floating_indices[i]] = perm[i]
            new_mem = ''.join(new_mem)
            all_mems.append(int(new_mem, 2))
            print(new_mem, int(new_mem, 2))

        if not floating_indices:
            all_mems.append(int(masked_mem, 2))

        val = int(l.split()[2])
        for new_mem in all_mems:
            lookup[new_mem] = val

print(sum(lookup.values()))