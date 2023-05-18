import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
iceberg = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
year = 0

def BFS(x, y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    queue = deque([[x, y]])
    visited[x][y] = 1

    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0:
                if iceberg[nx][ny] != 0:
                    visited[nx][ny] = 1
                    queue.append([nx, ny])
                else:
                    sea[cx][cy] += 1
    return 1

while True:
    visited = [[0 for _ in range(M)] for _ in range(N)]
    sea = [[0] * M for _ in range(N)]
    result = []

    for i in range(N):
        for j in range(M):
            if iceberg[i][j] != 0 and visited[i][j] == 0:
                result.append(BFS(i, j))

    for i in range(N):
        for j in range(M):
            iceberg[i][j] -= sea[i][j]
            if iceberg[i][j] < 0:
                iceberg[i][j] = 0

    if len(result) != 1:
        break
    year +=1

if len(result) > 1:
    print(year)
else:
    print(0)