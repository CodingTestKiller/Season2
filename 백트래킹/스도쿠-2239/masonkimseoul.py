import sys
from collections import deque

board = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(9)]
cnt = 0
q = deque()
for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            q.append([i, j])

def get_small(x, y):
    px = x // 3
    py = y // 3
    ar = []
    for i in range(px * 3, px * 3 + 3):
        for j in range(py * 3, py * 3 + 3):
            if board[i][j] != 0:
                ar.append(board[i][j])
    return ar

def get_row(x, y):
    ar = []
    for i in range(9):
        if board[x][i] != 0:
            ar.append(board[x][i])
    return ar

def get_col(x, y):
    ar = []
    for i in range(9):
        if board[i][y] != 0:
            ar.append(board[i][y])
    return ar

def DFS(x, y, q, d):
    global cnt
    cnt += 1
    numbers = list(range(1, 10))
    onboard = [] + get_small(x, y) + get_row(x, y) + get_col(x, y)
    numbers = [x for x in numbers if x not in onboard]

    for i in numbers:
        board[x][y] = i
        if len(q) == d:
            for j in range(9):
                for k in range(9):
                    print(board[j][k], end = ' ')
                print()
            return -1
        nx, ny = q[d][0], q[d][1]
        answer = DFS(nx, ny, q, d + 1)
        if answer == -1:
            return -1
        board[x][y] = 0

x, y = q.popleft()
DFS(x, y, q, 0)
