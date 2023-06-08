import sys

N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
answer = 0
form = {0: [0, -1, 1, 0], 1: [-1, 0, 0, -1], 2: [-1, 0, 0, 1], 3: [0, 1, 1, 0]}

def DFS(i, j, sum):
    global answer

    if j == M:
        i += 1
        j = 0

    if i == N:
        answer = max(answer, sum)
        return

    if visited[i][j] == 0:
        for k in range(4):
            f = form[k]
            x1, y1, x2, y2 = i + f[0], j + f[1], i + f[2], j + f[3]
            if 0 <= x1 < N and 0 <= y1 < M and 0 <= x2 < N and 0 <= y2 < M and visited[x1][y1] == 0 and visited[x2][y2] == 0:
                visited[x1][y1] = 1
                visited[x2][y2] = 1
                visited[i][j] = 1
                DFS(i,j + 1, sum + board[i][j] * 2 + board[x1][y1] + board[x2][y2])
                visited[x1][y1] = 0
                visited[x2][y2] = 0
                visited[i][j] = 0
    DFS(i, j + 1, sum)

DFS(0,0,0)
print(answer)