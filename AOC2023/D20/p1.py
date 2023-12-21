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
from itertools import permutations
from sympy.ntheory.modular import crt 
import hashlib
from time import sleep
from enum import Enum
import json

sys.setrecursionlimit(10000000)

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
g = defaultdict(list)
state = {}
flipflops = set()
flipflop_state = {}
conjunctions = set()
conjunctions_mem = defaultdict(lambda : LO)
broadcasters = set()
parent = defaultdict(list)
BROADCASTER = 'broadcaster'
LO = 0
HI = 1
ON = 2
OFF = 3
for line in fin:
    module, children = [c.strip() for c in line.split('->')]
    children = [c.strip() for c in children.split(',')]
    if module == BROADCASTER:
        broadcasters.add(module)
        for v in children:
            g[BROADCASTER].append(v)
            parent[v].append(BROADCASTER)
    else:
        if module[0] == '%': # flipflop
            flipflops.add(module[1:])
            flipflop_state[module[1:]] = OFF
        elif module[0] == '&': # conjunctions
            conjunctions.add(module[1:])
            conjunctions_mem[('-', module[1:])] = LO
        else:
            assert False
        for v in children:
            g[module[1:]].append(v)
            parent[v].append(module[1:])

q = deque([])

lo = 0
hi = 0

def cal():
    global lo, hi
    lo += 1
    # initially broadcaster sends out lo signal
    lo += len(g[BROADCASTER])
    for v in g[BROADCASTER]:
        q.append((BROADCASTER, v, LO))

    pprint(q)
    print(flipflops)
    print(conjunctions)
    while q:
        q_len = len(q)
        for _ in range(q_len):
            origin, u, signal = q.popleft()
            print(origin, u, signal, lo, hi)
            if u in flipflops:
                print(u, 'in flip flop')
                if signal == LO:
                    if flipflop_state[u] == ON:
                        flipflop_state[u] = OFF
                        lo += len(g[u])
                        for v in g[u]:
                            q.append((u, v, LO))
                    elif flipflop_state[u] == OFF:
                        flipflop_state[u] = ON
                        hi += len(g[u])
                        for v in g[u]:
                            q.append((u, v, HI))
            elif u in conjunctions:
                print(u, 'in conjunction')
                conjunctions_mem[(origin, u)] = signal
                for par in parent[u]:
                    print(par, conjunctions_mem[(par, u)])
                if all(conjunctions_mem[(ancestor, u)] == HI for ancestor in parent[u]):
                    lo += len(g[u])
                    for v in g[u]:
                        q.append((u,v,LO))
                else:
                    hi += len(g[u])
                    for v in g[u]:
                        q.append((u,v,HI))

for _ in range(1000):
    cal()
print(lo*hi)