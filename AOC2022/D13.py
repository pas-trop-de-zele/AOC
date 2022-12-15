import sys
from math import *
from pprint import pprint as pprint
from sympy.ntheory.modular import crt
import heapq
from copy import *
from collections import *
import functools
from itertools import *

# sys.setrecursionlimit(100000000)

from math import sqrt, ceil


fin = sys.stdin.read().strip().split("\n\n")

def isint(a):
    return isinstance(a, int)

def islist(a):
    return isinstance(a, list)

def compare(a, b):
    n = min(len(a), len(b))
    for i in range(n):
        if isint(a[i]) and isint(b[i]):
            if a[i] != b[i]:
                return a[i] - b[i]
        elif islist(a[i]) and islist(b[i]):
            ret = compare(a[i], b[i])
            if ret != 0:
                return ret
        else:
            if islist(a[i]):
                ret = compare(a[i], [b[i]])
            else:
                ret = compare([a[i]], b[i])
            if ret != 0:
                return ret
    if len(a) < len(b):
        return -1
    elif len(a) > len(b):
        return 1
    return 0

ret = 0
pairs = []
for i, pair in enumerate(fin):
    a, b = map(eval, pair.split("\n"))
    pairs.append(a)
    pairs.append(b)

pprint(pairs)
pairs.sort(key=functools.cmp_to_key(compare))
pprint(pairs)

ret = 1
for i, pair in enumerate(pairs):
    if pair == [[2]] or pair == [[6]]:
        ret *= i + 1 
print(ret)