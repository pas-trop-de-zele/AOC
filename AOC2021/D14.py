import sys
import math
from pprint import pprint as pprint
import heapq
from copy import *
from collections import *


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
s = fin[0]
directions = fin[1].split('\n')
lookup = {}
for l in directions:
    a, b = l.split('->')
    lookup[a.strip()] = b.strip()
pcount = defaultdict(lambda : 0)
char_counter = Counter(s)
for i in range(len(s) - 1):
    pair = s[i:i+2]
    pcount[pair] += 1
# pprint(pcount)
for i in range(40):
    new_counter = deepcopy(pcount)
    for pair, count in pcount.items():
        if pair in lookup:
            a, b = pair
            mid = lookup[pair]
            char_counter[mid] += count
            # print(pair, '->', mid)
            new_counter[f"{a}{mid}"] += count
            new_counter[f"{mid}{b}"] += count
            new_counter[pair] -= count
            if new_counter[pair] == 0:
                new_counter.pop(pair)
    pcount = new_counter
    # pprint(pcount)
    # pprint(char_counter)

lo, hi = math.inf, -math.inf
for char, count in char_counter.items():
    lo = min(lo, count)
    hi = max(hi, count) 
print(hi - lo)

# N B C C N B B B C B H C B
# NBBBCNCCNBBNBNBBCHBHHBCHB