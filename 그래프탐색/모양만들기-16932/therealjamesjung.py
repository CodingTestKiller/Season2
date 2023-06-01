from sys import stdin
from collections import deque

input = stdin.readline

n, m = [int(x) for x in input().split()]

board = [[int(x) for x in input().split()] for _ in range(n)]
visited = [[0] * m for _ in range(n)]
index_board = [[0] * m for _ in range(n)]

starts = {}
moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

max_cnt = 0


def bfs(x, y, tmp):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    cnt = 1
    while q:
        x, y = q.popleft()
        for move in moves:
            nx, ny = x + move[0], y + move[1]
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 1 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                q.append((nx, ny))
                tmp.append((nx, ny))
                cnt += 1
    return cnt


index = 1
for i in range(n):
    for j in range(m):
        if board[i][j] != 0 and not visited[i][j]:
            tmp = [(i, j)]
            cnt = bfs(i, j, tmp)
            for x, y in tmp:
                board[x][y] = cnt
                index_board[x][y] = index
            index += 1

result = 0

for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            tmp = 0
            indexes = set()
            for dx, dy in moves:
                nx, ny = i + dx, j + dy
                if 0 <= nx < n and 0 <= ny < m and board[nx][ny] != 0 and index_board[nx][ny] not in indexes:
                    tmp += board[nx][ny]
                    indexes.add(index_board[nx][ny])
            result = max(result, tmp + 1)


print(result)
