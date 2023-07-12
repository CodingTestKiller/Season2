import sys
from collections import defaultdict

N = int(sys.stdin.readline())
a = [0] * N
b = [0] * N
c = [0] * N
d = [0] * N
for i in range(N):
    a[i], b[i], c[i], d[i] = map(int, sys.stdin.readline().split())

num_add = defaultdict()
for i in range(len(c)):
    for j in range(len(d)):
        if c[i] + d[j] not in num_add:
            num_add[c[i] + d[j]] = 1
        else:
            num_add[c[i] + d[j]] += 1

answer = 0
for i in range(len(a)):
    for j in range(len(b)):
        if -a[i]-b[j] in num_add:
            answer += num_add[-a[i]-b[j]]
print(answer)