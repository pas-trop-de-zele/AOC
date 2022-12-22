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
import time

fin = sys.stdin.read().strip().split("\n")
graph = defaultdict(list)
cost = defaultdict(lambda: defaultdict(lambda: inf))
rate = {}
# One minute travel, one minute open, ret += flow * remains
for l in fin:
    _, u, _, _, r, _, _, _, _, *neis = l.split()
    r = int(r[5:-1])
    rate[u] = r
    neis = ''.join(neis).split(',')
    for v in neis:
        cost[u][v] = 1
        cost[v][u] = 1
        graph[u].append(v)

# Get the shortest distance for every pair of nodes
# Floyd Warshall
for k in cost:
    for u in cost:
        for v in cost:
            cost[u][v] = min(cost[u][v], cost[u][k] + cost[k][v])


worth_checking_out = [node for node in graph if rate[node] > 0]
opened = set()


# @functools.lru_cache(maxsize=None)
cache = {}


def dfs(u, opened_state, remains):
    if remains < 0:
        return -inf

    if remains == 0:
        return 0

    if (u, opened_state, remains) in cache:
        return cache[(u, opened_state, remains)]

    ret = 0
    for v in to_check:
        if v in opened:
            continue
        opened.add(v)
        take = rate[v]*(remains - cost[u][v] - 1) + \
            dfs(v, ''.join(sorted(opened)), remains - cost[u][v] - 1)
        opened.remove(v)
        ret = max(ret, take)
    cache[(u, opened_state, remains)] = ret
    return ret


start = time.time()
ret = 0
precomputed = {}
# Generate bit mask
# 0 represent human taken valves
# 1 represent elephant taken valves
# Then try all the possible pair, since a pair could be inverted
# Ex: 00001111 vs 11110000, we dont have to compute them twice so save result in precompute for the configuration to reuse
for mask in range(2**len(worth_checking_out)):
    print(mask)
    mask = bin(mask)[2:].zfill(len(worth_checking_out))
    human = [node for i, node in enumerate(
        worth_checking_out) if mask[i] == '0']
    elephant = [node for i, node in enumerate(
        worth_checking_out) if mask[i] == '1']

    to_check = set(human)
    opened = set()
    run_human = dfs('AA', '', 26) if tuple(
        to_check) not in precomputed else precomputed[tuple(to_check)]
    cache.clear()
    precomputed[tuple(to_check)] = run_human

    to_check = set(elephant)
    opened = set()
    run_elephant = dfs('AA', '', 26) if tuple(
        to_check) not in precomputed else precomputed[tuple(to_check)]
    cache.clear()
    precomputed[tuple(to_check)] = run_elephant

    ret = max(ret, run_human + run_elephant)

end = time.time()
print(ret)
print("FINISHED", end-start)
