from collections import deque
import copy
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]


dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


def Check(x, y):
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            kx = dx[i] + x
            ky = dy[i] + y
            if 0 <= kx < n and 0 <= ky < m and visit[kx][ky] and graph[kx][ky] > 0:
                visit[kx][ky] = False
                q.append((kx, ky))


def Melt():
    tmp = [i[:]for i in graph]
    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0:
                minus = 0
                for k in range(4):
                    kx = dx[k] + i
                    ky = dy[k] + j
                    if 0 <= kx < n and 0 <= ky < m and tmp[kx][ky] <= 0:
                        minus += 1
                graph[i][j] -= minus


year = 0

while True:
    visit = [[True for _ in range(m)] for _ in range(n)]
    lump = 0
    Melt()
    # for i in graph:
    #     print(i)
    # print()
    year += 1
    for i in range(n):
        for j in range(m):
            if graph[i][j] > 0 and visit[i][j]:
                visit[i][j] = False
                Check(i, j)
                lump += 1
                if lump >= 2:
                    print(year)
                    exit()
    if lump == 0:
        print(0)
        exit()
