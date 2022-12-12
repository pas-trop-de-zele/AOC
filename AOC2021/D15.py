import sys
import math
from pprint import pprint as pprint
import heapq
from copy import *
from collections import *
import functools

sys.setrecursionlimit(100000000)

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
for l in fin:
    m.append([int(c) for c in l])

HEIGHT = len(m)
WIDTH = len(m[0])
for r in range(HEIGHT):
    for c in range(WIDTH, WIDTH * 5):
        val = (m[r][c - WIDTH] + 1) % 10
        if val == 0: val = 1
        m[r].append(val)

HEIGHT = len(m)
WIDTH = len(m[0])
for r in range(HEIGHT, HEIGHT * 5):
    m.append([0 for _ in range(WIDTH)])
for c in range(WIDTH):
    for r in range(HEIGHT, HEIGHT * 5):
        val = (m[r - HEIGHT][c] + 1) % 10
        if val == 0: val = 1
        m[r][c] = val
# debM(m)
HEIGHT = len(m)
WIDTH = len(m[0])
g = defaultdict(list)
for r in range(HEIGHT):
    for c in range(WIDTH):
        for dy, dx in MOVES_ADJACENT:
            rr = r + dy
            cc = c + dx
            if not 0 <= rr < HEIGHT or not 0 <= cc < WIDTH:
                continue
            w = m[rr][cc]
            g[(r, c)].append((rr, cc, w))
minh = []
dist = defaultdict(lambda : math.inf)
seen = set()
heapq.heappush(minh, (0, 0, 0))
while minh:
    root_dist, r, c = heapq.heappop(minh)
    if (r, c) in seen:
        continue
    dist[(r, c)] = root_dist
    seen.add((r, c))
    for rr, cc, w in g[(r, c)]:
        if (rr, cc) in seen:
            continue
        heapq.heappush(minh, (min(dist[(rr, cc)], root_dist + w),rr,cc))
print(dist[(HEIGHT-1, WIDTH-1)])
