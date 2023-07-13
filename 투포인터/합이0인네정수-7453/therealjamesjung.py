from bisect import bisect_left, bisect_right
from sys import stdin

input = stdin.readline

n = int(input())

a = []
b = []
c = []
d = []

for _ in range(n):
    x, y, z, w = [int(x) for x in input().split()]
    a.append(x)
    b.append(y)
    c.append(z)
    d.append(w)

A_B = {}

for i in range(n):
    for j in range(n):
        try:
            A_B[a[i] + b[j]] += 1
        except KeyError:
            A_B[a[i] + b[j]] = 1

cnt = 0

for i in range(n):
    for j in range(n):
        try:
            cnt += A_B[-(c[i] + d[j])]
        except KeyError:
            pass

print(cnt)