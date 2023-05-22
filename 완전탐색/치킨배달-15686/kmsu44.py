import sys
from collections import deque
from itertools import combinations
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
chicken = []
house = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            house.append((i, j))
        if graph[i][j] == 2:
            chicken.append((i, j))
            graph[i][j] = 0


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


chicken_list = list(combinations(chicken, m))


def findChickendistance(hx, hy, chicken_list):
    distance = sys.maxsize
    for x, y in chicken_list:
        distance = min(distance, abs(hx-x) + abs(hy-y))
    return distance


res = sys.maxsize


for i in chicken_list:
    tmp = 0
    for x, y in house:
        tmp += findChickendistance(x, y, i)
    res = min(tmp, res)

print(res)
