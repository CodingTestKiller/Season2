import sys
sys.setrecursionlimit(10**6)
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]

shape = 0


def DFS(x, y):
    global res
    global cnt
    res.append((x, y))
    for i in range(4):
        next_x = dx[i] + x
        next_y = dy[i] + y
        if 0 <= next_x < n and 0 <= next_y < m and visit[next_x][next_y][1] == -1 and graph[next_x][next_y] == 1:
            visit[next_x][next_y] = (-1, 0)
            DFS(next_x, next_y)


cnt = 0
visit = [[(-1, -1)] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        res = []
        cnt = 0
        if graph[i][j] == 1 and visit[i][j][1] == -1:
            visit[i][j] = (-1, 0)
            DFS(i, j)
        cnt = len(res)
        for x, y in res:
            visit[x][y] = (shape, cnt)
        shape += 1

ans = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            shape_set = set()
            cnt = 1
            for k in range(4):
                x = dx[k] + i
                y = dy[k] + j
                if 0 <= x < n and 0 <= y < m:
                    if visit[x][y][0] not in shape_set and visit[x][y][1] != -1:
                        flag = 1
                        shape_set.add(visit[x][y][0])
                        cnt += visit[x][y][1]
            ans = max(ans, cnt)

print(ans)
