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

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

def lcm_of_list(numbers):
    result = 1
    for num in numbers:
        result = lcm(result, num)
    return result

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
sent = {}
BROADCASTER = 'broadcaster'
LO = 0
HI = 1
ON = 2
OFF = 3

def initialize():
    global g, state, flipflops, flipflop_state, conjunctions, conjunctions_mem, broadcasters, parent, sent
    g = defaultdict(list)
    state = {}
    flipflops = set()
    flipflop_state = {}
    conjunctions = set()
    conjunctions_mem = defaultdict(lambda : LO)
    broadcasters = set()
    parent = defaultdict(list)
    sent = {}
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

def cal(register):
    global lo, hi
    q = deque([])
    # initially broadcaster sends out lo signal
    for v in g[BROADCASTER]:
        q.append((BROADCASTER, v, LO))

    while q:
        q_len = len(q)
        for _ in range(q_len):
            origin, u, signal = q.popleft()
            if origin == register and u == 'dn' and signal == HI:
                return True
            if u in flipflops:
                if signal == LO:
                    if flipflop_state[u] == ON:
                        flipflop_state[u] = OFF
                        for v in g[u]:
                            q.append((u, v, LO))
                    elif flipflop_state[u] == OFF:
                        flipflop_state[u] = ON
                        for v in g[u]:
                            q.append((u, v, HI))
            elif u in conjunctions:
                conjunctions_mem[(origin, u)] = signal
                if all(conjunctions_mem[(ancestor, u)] == HI for ancestor in parent[u]):
                    for v in g[u]:
                        q.append((u,v,LO))
                else:
                    for v in g[u]:
                        q.append((u,v,HI))
    return False

nums = []
for register in ['dd', 'fh', 'xp', 'fc']:
    initialize()
    for i in range(100000000000):
        done = cal(register)
        if done:
            nums.append(i+1)
            break
print(nums)
print(lcm_of_list(nums))

"""
&rx is a conjuctions
rx parents is also a conjunction(&dn) (how many path to the beginning)
all dn's parents would have to also be hi
question becomes how button needed to pressed before all of &dns'a parents becomes high

if we can find all the path from source to rx, we can find the one that requires the least button press
given a path, how to find the number of button presses it takes?

a conjunction to get low pulse would require:
    - conjuctions ancestors, any of there ancestors got a LO will trigger them to send a HI
    - flip flop ancestors have to send out high pulse:
        - have to receive a low pulse while being off

let see the path to BROADCASTER from 'rx'
too many paths....


rx <- conjunctions
dn <- conjunctions (need to receive ALL HI -> sends LO)
['dd', 'fh', 'xp', 'fc'] <- conjunctions (need to each receive LO -> sends HI)
['rs']['bd']['pm']['cc'] <- conjunctions (need to each receive HI -> sends LO)

----- ALL BELOW ARE FLIPFLOPS -----
rs ['jx', 'qs', 'qq', 'hd', 'cl', 'zx', 'rh', 'sg']
bd ['dj', 'br', 'zc', 'nz', 'gz', 'ng', 'kb', 'nf', 'jq', 'jk']
pm ['mx', 'xg', 'zd', 'gj', 'cf', 'pc', 'vf', 'nr', 'lt']
cc ['mj', 'cj', 'cd', 'pj', 'cq', 'nt', 'ln', 'mn']

use lcm to look for cycle of when each of these would all be off and sends out high pulse 
problem is using the cycle of each would not be accurate since they do not start at the point
there is an offset associate which makes the meeting point be lower than it actually is

potentially uses crt? since there is offset
however, it is not just simple cycle since its has ranges

"""

# options = [
#    ['jx', 'qs', 'qq', 'hd', 'cl', 'zx', 'rh', 'sg'],
#    ['dj', 'br', 'zc', 'nz', 'gz', 'ng', 'kb', 'nf', 'jq', 'jk'],
#    ['mx', 'xg', 'zd', 'gj', 'cf', 'pc', 'vf', 'nr', 'lt'],
#    ['mj', 'cj', 'cd', 'pj', 'cq', 'nt', 'ln', 'mn'],
# ]
    
# for option in options:
#     cycles = []
#     for u in option:
#         initialize()
#         occur = [(-1, -1)]
#         for i in range(1, 10000000000):
#             cal()
#             if flipflop_state[u] != occur[-1][0]:
#                 occur.append([flipflop_state[u],i])
#             if len(occur) > 4 and occur[-1][0] == OFF:
#                 break
#         cycles.append(occur[-1][1] - occur[-3][1])
#     print(cycles, lcm_of_list(cycles))
