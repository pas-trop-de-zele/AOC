from math import sqrt, ceil


def fac(n):
    ret = []
    while n % 2 == 0:
        ret.append(2)
        n /= 2
    for i in range(3, n, 2):
        if i * i > n:
            break
        while n % i == 0:
            if n == 1:
                break
            ret.append(i)
            n /= i
    if (n > 1):
        ret.append(n)
    print(ret)


n = input()
n = int(n)
fac(n)
