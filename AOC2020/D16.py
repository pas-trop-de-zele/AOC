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

def fac(n):
    ret = []
    while n % 2 == 0:
        if not ret:
            ret.append(2)
        n //= 2
    for i in range(3, n, 2):
        if i * i > n:
            break
        while n % i == 0:
            if not ret or ret[-1] != i:
                ret.append(i)
            n //= i
        if n == 1:
            break
    if (n > 1):
        ret.append(n)
    return ret

class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size
        self.components = size
        
    def find(self, x):
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        if not self.is_connected(x, y):
            rootX = self.root[x]
            rootY = self.root[y]
            if self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            elif self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1
            self.components -= 1

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)

    def distinct_components(self):
        return self.components

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

def is_valid(num):
    for ranges in valids.values():
        if ranges[0][0] <= num <= ranges[0][1] or ranges[1][0] <= num <= ranges[1][1]:
            return True
    return False

def get_potential_fields(num):
    ret = set()
    for field, ranges in valids.items():
        if ranges[0][0] <= num <= ranges[0][1] or ranges[1][0] <= num <= ranges[1][1]:
            ret.add(field)
    return ret

fields = fin[0].split("\n")
my_tickets = [int(c) for c in fin[1].split("\n")[1].split(',')]
nearby = fin[2].split("\n")[1:]
valids = defaultdict(list)
field_names = []
field_ranges = []

for field in fields:
    field_name = field[:field.find(':')]
    field_names.append(field_name)
    field = field[field.find(':') + 1:].split()
    A, B = field[0], field[2]
    Astart, Aend = [int(c) for c in A.split("-")]
    Bstart, Bend = [int(c) for c in B.split("-")]
    field_ranges.append([(Astart, Aend), (Bstart, Bend)])
    valids[field_name].append((Astart, Aend))
    valids[field_name].append((Bstart, Bend))

valid_tickets = []
for tickets in nearby:
    tickets = [int(c) for c in tickets.split(',')]
    all_valid = True
    for i, ticket in enumerate(tickets):
        if not is_valid(ticket):
            all_valid = False
            break
    if all_valid:
        valid_tickets.append(tickets)

n = len(field_ranges)
possible_fields = [[] for _ in range(n)]
for field_index in range(n):
    for _, ranges in enumerate(field_ranges):
        fit_for_all = True
        for tickets in valid_tickets:
            if not ranges[0][0] <= tickets[field_index] <= ranges[0][1] \
                and not ranges[1][0] <= tickets[field_index] <= ranges[1][1]:
                fit_for_all = False
                break

        if fit_for_all:
            possible_fields[field_index].append(_)
print(possible_fields)
final_position = [-1] * n
for _ in range(n):
    for i, pf in enumerate(possible_fields):
        if len(pf) == 1:
            to_remove = pf[-1]
            final_position[i] = to_remove
            for field in possible_fields:
                if to_remove in field:
                    field.remove(to_remove)

ret = 1
for i, ticket in enumerate(my_tickets):
    field_name = field_names[final_position[i]]
    if field_name.find('departure') == 0:
        ret *= ticket
print(ret)

