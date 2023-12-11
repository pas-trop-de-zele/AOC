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
counters = [Counter() for _ in range(8)]
counter_id = 0
for line_id in range(1, len(fin)):
    print("AT", line_id)
    counter_id += 1
    line = fin[line_id]
    line = line.split("\n")
    source, dest = line[0].split()[0].split("-to-")
    for entry_id in range(1, len(line)):
        deststart, sourcestart, rangelen = [int(c) for c in line[entry_id].strip().split()]
        for inc in range(rangelen+1):
            # print(sourcestart+inc, deststart+inc)
            counters[counter_id][sourcestart+inc] = deststart+inc
# ret = math.inf
# # print(counters)
# for seed in seeds:
#     print(seed)
#     cur = seed
#     # print(cur)
#     for counter_id in range(1, 8): 
#         if cur not in counters[counter_id]:
#             cur = cur
#         else:
#             cur = counters[counter_id][cur]
#         # print(cur)
#     ret = min(ret, cur)
# print(ret)