import sys
import math
import heapq
from collections import deque, defaultdict


def debM(m):
    for r in m:
        for c in r:
            print(c, end='')
        print()
    print()


MOVES_ADJACENT = [[1, 0], [0, 1], [-1, 0], [0, -1]]
MOVES_ALL = [[1, 0], [1, 1], [0, 1], [-1, 1],
             [-1, 0], [-1, -1], [0, -1], [1, -1]]
fin = sys.stdin.read().strip().split('\n\n')
spots = fin[0].split("\n")
directions = fin[1].split("\n")
h = w = 0
for l in spots:
    c, r = [int(a) for a in l.split(',')]
    h = max(h, r + 1)
    w = max(w, c + 1)
m = [['.' for _ in range(w)] for _ in range(h)]
for l in spots:
    c, r = [int(a) for a in l.split(',')]
    m[r][c] = '#'
# debM(m)
print(h, w)
for d in directions:
    _, _, d = d.split()
    axis, a = d.split('=')
    a = int(a)
    print(axis, a)
    if axis == 'y':
        start = a - (h-1-a)
        for r in range(start, a):
            for c in range(w):
                if m[h-1-(r-start)][c] == '#':
                    m[r][c] = '#'
        h = a
    else:
        start = a - (w-1-a)
        for c in range(start, a):
            for r in range(h):
                if m[r][w-1-(c-start)] == '#':
                    m[r][c] = '#'
        w = a
    cur = 0
    for r in range(h):
        for c in range(w):
            if m[r][c] == '#':
                cur += 1
    print(cur)
for r in range(h):
    for c in range(w):
        print(m[r][c], end=' ')
    print()
