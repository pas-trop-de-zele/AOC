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


def is_same(lookup):
    times = set()
    for start in lookup.values():
        times.add(start)
    return len(times) == 1 

MOVES_ADJACENT = [[1, 0], [0, 1], [-1, 0], [0, -1]]
MOVES_ALL = [[1, 0], [1, 1], [0, 1], [-1, 1],
             [-1, 0], [-1, -1], [0, -1], [1, -1]]
fin = sys.stdin.read().strip().split("\n\n")

class Monkey:
    def __init__(self, monkey, items, operation, val, divisible, true_monkey, false_monkey):
        self.monkey = monkey
        self.items = items
        self.operation = operation
        self.val = val
        self.divisible = divisible
        self.true_monkey = true_monkey
        self.false_monkey = false_monkey

def get_monkey_inventory(monkeys):
    for i, monkey in enumerate(monkeys):
        print(i, ": ", monkey.items)

monkeys = []
for l in fin:
    lines = l.split("\n")
    monkey = int(lines[0][-2])
    items = [int(c) for c in lines[1][lines[1].find(':') + 2:].split(", ")]
    operation = lines[2][lines[2].find(':') + 2:].split()[3]
    # could be old
    val = lines[2][lines[2].find(':') + 2:].split()[4]
    divisible = int(lines[3][lines[3].find(':') + 2:].split()[2])
    true_monkey = int(lines[4][lines[4].find(':') + 2:].split()[3])
    false_monkey = int(lines[5][lines[5].find(':') + 2:].split()[3])
    monkeys.append(Monkey(monkey, items, operation, val, divisible, true_monkey, false_monkey))

inspect_count = Counter()
for _ in range(10000):
    for i, monkey in enumerate(monkeys):
        for item in monkey.items:
            inspect_count[i] += 1
            
            val = item if monkey.val == 'old' else int(monkey.val) 

            if monkey.operation == '+':
                item += val
            elif monkey.operation == '*':
                item *= val

            mods = [11,19,5,3,13,17,7,2]
            remainders = [item % mod for mod in mods]
            reduced_item = crt(mods, remainders)[0]
            if item % monkey.divisible == 0:
                monkeys[monkey.true_monkey].items.append(reduced_item)
            else:
                monkeys[monkey.false_monkey].items.append(reduced_item)

        monkey.items.clear()
    print()
get_monkey_inventory(monkeys)
inspects = list(inspect_count.values())
inspects.sort()
print(inspects)
print(inspects[-1] * inspects[-2])
