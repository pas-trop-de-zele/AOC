import sys
from math import *
from pprint import pprint as pprint
from sympy.ntheory.modular import crt
import heapq
from copy import *
from collections import *
import functools
from itertools import *
from math import sqrt, ceil
import threading
import cmath  

fin = sys.stdin.read().strip().split("\n")
graph = defaultdict(list)
rate = {}
# One minute travel, one minute open, ret += flow * remains
for l in fin:
    _, u, _, _, r, _, _, _, _, *neis = l.split()
    r = int(r[5:-1])
    rate[u] = r
    neis = ''.join(neis).split(',') 
    for v in neis:
        graph[u].append(v)

opened = set(['AA'])
# @functools.lru_cache(maxsize=None)
# def dfs(u, opened_state, remains):
#     if remains < 0:
#         return -inf

#     if remains == 0:
#         return 0

#     ret = 0
#     for v in graph[u]:
#         take, skip = 0, 0
#         if v not in opened:
#             opened.add(v)
#             take = rate[v]*(remains - 2) + dfs(v, ''.join(sorted(opened)), remains - 2)
#             opened.remove(v)

#         skip = dfs(v, ''.join(sorted(opened)), remains - 1)
#         ret = max(ret, max(take, skip))
#     return ret
dp = defaultdict(int)
def dfs(u, opened_state, remains):
    if (opened_state, remains) in dp:
        return dp[(u, opened_state, remains)]

    if remains < 0:
        return -inf

    if remains == 0:
        return 0
    
    ret = 0
    for v in graph[u]:
        take, skip = 0, 0
        if v not in opened:
            opened.add(v)
            take = rate[v]*(remains - 2) + dfs(v, ''.join(sorted(opened)), remains - 2)
            opened.remove(v)

        skip = dfs(v, ''.join(sorted(opened)), remains - 1)
        ret = max(ret, max(take, skip))
    dp[(u, opened_state, remains)] = ret
    return ret
print(dfs('AA', '', 30))
    
