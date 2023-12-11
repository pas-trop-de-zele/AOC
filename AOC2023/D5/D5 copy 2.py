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
seeds = [int(c) for c in fin[0][7:].strip().split()]
new_seeds = []
for i in range(0, len(seeds), 2):
    for delta in range(seeds[i+1]):
        new_seeds.append(seeds[i]+delta)
seeds = list(new_seeds)
ret = math.inf
for seed in seeds:
    cur = seed
    
    counters = [Counter() for _ in range(8)]
    counter_id = 0
    for line_id in range(1, len(fin)):
        # print("CUR", cur)
        counter_id += 1
        line = fin[line_id]
        line = line.split("\n")
        source, dest = line[0].split()[0].split("-to-")
        for entry_id in range(1, len(line)):
            deststart, sourcestart, rangelen = [int(c) for c in line[entry_id].strip().split()]
            # print(deststart, sourcestart, rangelen)
            if sourcestart <= cur < sourcestart+rangelen:
                delta = cur - sourcestart
                cur = deststart + delta
                break
            else:
                cur = cur
    ret = min(ret, cur)
print(ret)