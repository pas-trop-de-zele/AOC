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

lookup = defaultdict(int)


seen_count = Counter()


def is_valid(n):
    if is_zeroed(n):
        return False

    lookup = defaultdict(int)
    i = 0
    n = str(n)

    def alu(instr):
        nonlocal i
        instr = instr.split()

        if len(instr) == 2:
            a = instr[1]
            lookup[a] = int(n[i])
            i += 1
        else:
            op, a, b = instr
            if op == 'add':
                lookup[a] += lookup[b] if b in 'wxzy' else int(b)
            elif op == 'mul':
                lookup[a] *= lookup[b] if b in 'wxzy' else int(b)
            elif op == 'div':
                lookup[a] //= lookup[b] if b in 'wxzy' else int(b)
            elif op == 'mod':
                lookup[a] %= lookup[b] if b in 'wxzy' else int(b)
            elif op == 'eq':
                lookup[a] = lookup[a] == lookup[b] if b in 'wxzy' else int(b)

    for l in fin:
        # print(n, l)
        alu(l)
    assert(i == 14)
    if (lookup['z']) in seen_count:
        print("SEEN", n, seen_count[(lookup['z'])], (lookup['z']))
    seen_count[(lookup['z'])] += 1
    return lookup['z'] == 0


def is_zeroed(n):
    while n:
        if n % 10 == 0:
            return True
        n //= 10
    return False


fin = sys.stdin.read().strip().split("\n")


def solve():
    for n in range(10**14 - 1, 10**13 - 1, -1):
        if is_valid(n):
            return n


print(solve())
