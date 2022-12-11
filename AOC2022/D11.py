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
# sys.setrecursionlimit(100000000)


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

            # CHINESE REMAINDER THEOREM
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
