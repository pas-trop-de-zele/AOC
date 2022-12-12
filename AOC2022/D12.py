import sys
from math import *
from pprint import pprint as pprint
from sympy.ntheory.modular import crt
import heapq
from copy import *
from collections import *
import functools
from itertools import *

# sys.setrecursionlimit(100000000)

from math import sqrt, ceil

def fac(n):
    ret = []
    while n % 2 == 0:
        if not ret:
            ret.append(2)
        n //= 2
    for i in range(3, n, 2):
        if i * i > n:
            break
        while n % i == 0:
            if not ret or ret[-1] != i:
                ret.append(i)
            n //= i
        if n == 1:
            break
    if (n > 1):
        ret.append(n)
    return ret

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


MOVES_ADJACENT = [[1, 0], [0, 1], [-1, 0], [0, -1]]
MOVES_ALL = [[1, 0], [1, 1], [0, 1], [-1, 1],
             [-1, 0], [-1, -1], [0, -1], [1, -1]]
fin = sys.stdin.read().strip().split('\n')
m = []

"""
where a is the lowest elevation
b is the next-lowest=
and so on up to the highest elevation, z.

z -> a elevation

You'd like to reach E, but to save energy, you should do it in as few steps as possible.

you can move exactly one square up, down, left, or right. MOVES_ADJACENT

destination should be at most 1 higher
S starts a elevation
"""
for l in fin:
    m.append([c for c in l])
H = len(m)
W = len(m[0])

# find start
def find_start():
    for r in range(H):
        for c in range(W):
            if m[r][c] == 'S':
                return (r, c)

# find end
def find_end():
    for r in range(H):
        for c in range(W):
            if m[r][c] == 'E':
                return (r, c)

start = find_start()
end = find_end()
# Set these points to a and z
m[start[0]][start[1]] = 'a'
print(m[start[0]][start[1]])
m[end[0]][end[1]] = 'z'
print(m[end[0]][end[1]])

lookup = defaultdict(list)
for r in range(H):
    for c in range(W):
        for dy, dx in MOVES_ADJACENT:
            rr = r + dy
            cc = c + dx
            if not 0 <= rr < H or not 0 <= cc < W or ord(m[rr][cc]) - ord(m[r][c]) > 1:
                continue
            lookup[(r, c)].append((rr, cc, 1))

ret = inf
for r in range(H):
    for c in range(W):
        if m[r][c] != 'a':
            continue

        start = [r, c]
        final_dist = defaultdict(lambda : inf)
        minh = []
        heapq.heappush(minh, (0, start[0], start[1]))
        seen = set()
        while minh:
            dist_from_root, r, c = heapq.heappop(minh)
            final_dist[(r, c)] = dist_from_root
            if (r, c) in seen:
                continue

            seen.add((r, c))
            for rr, cc, w in lookup[(r, c)]:
                if (rr, cc) in seen:
                    continue
                heapq.heappush(minh, (min(dist_from_root + w, final_dist[(rr, cc)]), rr, cc))
        # print(final_dist)
        ret = min(ret, final_dist[tuple(end)])
print(ret)