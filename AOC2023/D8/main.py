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

fin = sys.stdin.read().strip().split("\n\n")
instruction = fin[0]
g = defaultdict(list)
C = []
for line in fin[1].split('\n'):
    u = [c.strip() for c in line.split('=')][0]
    l,r = [c.strip() for c in line.split('=')][1].split(', ')
    l = l[1:]
    r = r[:-1]
    g[u] = [l,r]
    if u[-1] == 'A':
        C.append(u)
print(C)
ret = 0
lcm = []
for cur in C:
    count = 0
    while not cur[-1] == 'Z':
        for c in instruction:
            count += 1
            if c=='L':
                cur = g[cur][0]
            else:
                cur = g[cur][1]
            if cur[-1] == 'Z':
                print("HERE", count)
                lcm.append(count)
                break
from math import gcd
ret = 1
for i in lcm:
    ret = ret*i//gcd(ret, i)
print(ret)