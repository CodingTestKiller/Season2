import sys

from collections import deque
from itertools import permutations

graph = [[list(map(int, sys.stdin.readline().split())) for _ in range(5)] for _ in range(5)]
visited = [[[0] * 5 for _ in range(5)] for _ in range(5)]
vcnt = 0

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

answer = float("inf")

def BFS(p):
    global vcnt, answer
    board = []
    for i in p:
        board.append(graph[i])
    vcnt +=1
    s = [0, 0, 0]
    e = [4, 4, 4]
    if board[s[0]][s[1]][s[2]] != 1 or board[e[0]][e[1]][e[2]] != 1:
        return

    vcnt += 1
    q = deque([s+[0]])
    visited[0][s[0]][s[1]] = vcnt
    while q:
        x, y, z, cnt = q.pop()
        if cnt >= answer:
            continue
        if e[0] == x and e[1] == y and e[2] == z:
            answer = min(answer, cnt)
            break

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if check(nx, ny, nz, board):
                visited[nx][ny][nx] = vcnt
                q.appendleft([nx, ny, nz, cnt + 1])

def check(x, y, z, board):
    if x < 0 or y < 0 or z < 0 or x >= 5 or y >= 5 or z >= 5:
        return False
    elif board[x][y][z] == 0:
        return False
    elif visited[x][y][z] == vcnt:
        return False
    return True

def rotate(x):
    tmp = []
    for i in graph[x]:
        row = []
        for j in i:
            row.append(j)
        tmp.append(row)

    for i in range(5):
        for j in range(5):
            graph[x][j][4-i] = tmp[i][j]

def make_stack(st, idx):
    if answer == 12:
        return
    if idx == 5:
        BFS(st)
        return
    for _ in range(4):
        rotate(st[idx])
        make_stack(st, idx + 1)

for i in permutations(range(5), 5):
    make_stack(i, 0)

if answer == float("inf"):
    print("-1")
else:
    print(answer)