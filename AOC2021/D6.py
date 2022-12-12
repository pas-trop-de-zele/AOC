import sys
import math
from pprint import pprint as pprint
import heapq
from copy import *
from collections import *


def debM(m):
    for r in m:
        for c in r:
            print(c, end=' ')
        print()
    print()


MOVES_ADJACENT = [[1, 0], [0, 1], [-1, 0], [0, -1]]
MOVES_ALL = [[1, 0], [1, 1], [0, 1], [-1, 1],
             [-1, 0], [-1, -1], [0, -1], [1, -1]]
fin = sys.stdin.read().strip()
nums = [int(c) for c in fin.split(',')]
counter = [0] * 9
for c in nums:
    counter[c] += 1
for i in range(256):
    new = [0] * 9
    new[6] += counter[0]
    new[8] += counter[0]
    for i in range(1,9):
        new[i - 1] += counter[i]
    counter = new
    print(sum(counter))