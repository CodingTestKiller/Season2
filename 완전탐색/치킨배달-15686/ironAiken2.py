from sys import stdin
input = stdin.readline
from itertools import combinations

n, m = [int(x) for x in input().split()]
_map = [[int(x) for x in input().split()] for _ in range(n)]


house = []
store = []
for i in range(n):
    for j in range(n):
        if _map[i][j] == 0:
            continue
        if _map[i][j] == 1:
            house.append((i,j))
        if _map[i][j] == 2:
            store.append((i,j))

dist = [[] for _ in range(len(house))]
index = [i for i in range(len(store))]

for i, h in enumerate(house):
    for s in store:
        dist[i].append(abs(h[0]-s[0]) + abs(h[1] - s[1]))

comb = list(combinations(index, m))

ans = 2500 * 2500
for com in comb:
    flag = 0
    for d in dist:
        _min = 100000
        for i in com:
            _min = min(_min, d[i])
        flag += _min

    ans = min(ans, flag)

print(ans)
        