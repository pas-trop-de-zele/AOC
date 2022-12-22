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
"""
Get the path that each number was made from

for each num, store the operation that build them

"""
def isnum(a):
    return isinstance(a, int) or isinstance(a, float)
lookup = {}
operations = set()
origin = {}
fin = sys.stdin.read().strip().split("\n")
FINAL = ()
for l in fin:
    l = l.split()

    a = l[0][:-1]
    # lone monkey
    if len(l) == 2:
        val = int(l[1])
        lookup[a] = val
        origin[a] = str(val)
    else:
        left, op, right = l[1], l[2], l[3]
        origin[a] = f"({left} {op} {right})"
        if a == 'root':
            FINAL = (left, right)  
        operations.add((a, left, op, right))

while operations:
    new = set()
    new_lookup = deepcopy(lookup)
    for b, left, op, right in operations:
        newleft, newright = left, right
        is_solved = False
        
        for a, val in lookup.items():
            if left == a:
                newleft = val
            elif right == a:
                newright = val
        
            if isnum(newleft) and isnum(newright):
                new_lookup[b] = eval(f"{newleft}{op}{newright}")
                is_solved = True
                break

        if not is_solved:    
            new.add((b, newleft, op, newright))

    operations = new
    lookup = new_lookup

def parse(x):
    if x == 'humn':
        return x

    if len(origin[x].split()) == 1:
        return origin[x]

    l, op, r = origin[x].split()
    return f"({parse(l[1:])} {op} {parse(r[:-1])})"

a = parse(FINAL[0])
b = parse(FINAL[1])

from sympy import symbols, solve

humn = symbols('humn')
expr = a + '-' + b
sol = solve(expr)
print(sol)