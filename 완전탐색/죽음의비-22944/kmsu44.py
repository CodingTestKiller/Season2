# 11시 50분 시작
import sys
from collections import deque
n, h, d = map(int, input().split())
graph = [[i for i in input()] for _ in range(n)]


visit = [[0 for _ in range(n)] for _ in range(n)]


def BFS(start, life, umbrella):
    x, y = start
    q = deque()
    q.append((x, y, life, 0, 0))
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    while q:
        x, y, h, u, cnt = q.popleft()
        for i in range(4):
            kx = dx[i] + x
            ky = dy[i] + y
            if 0 <= kx < n and 0 <= ky < n:
                if graph[kx][ky] == 'E':
                    return cnt+1
                nh = h
                nu = u
                if graph[kx][ky] == 'U':
                    nu = umbrella
                if nu == 0:
                    nh -= 1
                else:
                    nu -= 1
                if visit[kx][ky] < nh:
                    visit[kx][ky] = nh
                    q.append((kx, ky, nh, nu, cnt+1))
    return -1


for i in range(n):
    for j in range(n):
        if graph[i][j] == 'S':
            start = (i, j)
            visit[i][j] = h

print(BFS(start, h, d))
