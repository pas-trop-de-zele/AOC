import sys
import math
from pprint import pprint as pprint
import heapq
from copy import *
from collections import *
import functools

sys.setrecursionlimit(100000000)
def debM(m):
    for r in m:
        for c in r:
            print(c, end=' ')
        print()
    print()


MOVES_ADJACENT = [[1, 0], [0, 1], [-1, 0], [0, -1]]
MOVES_ALL = [[1, 0], [1, 1], [0, 1], [-1, 1],
             [-1, 0], [-1, -1], [0, -1], [1, -1]]
fin = sys.stdin.read().strip().split('\n')
m = []
for l in fin:
    m.append([int(c) for c in l])
h = len(m)
w = len(m[0])
g = defaultdict(list)
# for r in range(h):
#     for c in range(w):
#         print(r, c)
for r in range(h):
    for c in range(w):
        print(r, c)
        for dy, dx in MOVES_ADJACENT:
            rr = r + dy
            cc = c + dx
            print("TRY ", rr, cc)
            if not 0 <= rr < h or not 0 <= cc < w:
                continue
            print("CHECK", rr, cc)
            w = m[rr][cc]
            g[(r, c)].append((w, rr, cc))
minh = []
heapq.heappush(minh, (0, 0, 0))
