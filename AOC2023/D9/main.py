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
g = defaultdict(list)
par = Counter()
ancestor = defaultdict(list)
for line in fin:
    line = line.split()
    u = line[1]
    v = line[7]
    g[u].append(v)
    ancestor[v].append(u)
    par[v] += 1


def cal(x):
    return TIME_CONSTANT + (ord(x) - ord('A')) + 1

N = 5
TIME_CONSTANT = 60
workers = []
Q = deque([u for u in g if par[u] == 0])
T = -1

def assign_workers():
    global Q
    Q = deque(sorted(list(Q)))
    while len(workers) < N and Q:
        u = Q.popleft()
        workers.append((T + cal(u), u))

assign_workers()
while workers:
    print(workers)
    done_time, u = min(workers)
    T = done_time
    print("Done work", u, "at", done_time)
    workers = [x for x in workers if x != (done_time, u)]
    for v in g[u]:
        par[v] -= 1
        if par[v] == 0:
            print('from', u, 'to', v, done_time, cal(v))
            Q.append(v)
    print(Q)
    assign_workers()
