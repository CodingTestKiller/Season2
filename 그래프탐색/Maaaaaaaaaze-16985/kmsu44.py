# 11시 5분 시작
from itertools import permutations
from collections import deque
import copy

board = []
for i in range(5):
    tmp = [list(map(int, input().split())) for _ in range(5)]
    board.append(tmp)


def Rotate(board):
    rotated_board = [[] for _ in range(5)]
    for j in range(0, 5):
        for i in range(4, -1, -1):
            rotated_board[j].append(board[i][j])
    return rotated_board


floor = [0, 1, 2, 3, 4]
floor_index = list(permutations(floor, 5))

rotate_index = []
for a in range(4):
    for b in range(4):
        for c in range(4):
            for d in range(4):
                for e in range(4):
                    rotate_index.append([a, b, c, d, e])


def BFS(matrix, x, y, z):
    dx = [0, 0, -1, 1, 0, 0]
    dy = [-1, 1, 0, 0, 0, 0]
    dz = [0, 0, 0, 0, 1, -1]
    q = deque()
    q.append((0, 0, 0, 0))
    visit[0][0][0] = False
    while q:
        x, y, z, cnt = q.popleft()
        if z == 4 and y == 4 and x == 4:
            return cnt
        for i in range(6):
            kx = dx[i] + x
            ky = dy[i] + y
            kz = dz[i] + z
            if 0 <= kx < 5 and 0 <= ky < 5 and 0 <= kz < 5 and visit[kz][kx][ky] and matrix[kz][kx][ky] == 1:
                visit[kz][kx][ky] = False
                q.append((kx, ky, kz, cnt+1))
    return -1


res = 125
flag = False
for floor in floor_index:
    a, b, c, d, e = floor
    for rotate in rotate_index:
        a_r, b_r, c_r, d_r, e_r = rotate
        A = copy.deepcopy(board[a])
        B = copy.deepcopy(board[b])
        C = copy.deepcopy(board[c])
        D = copy.deepcopy(board[d])
        E = copy.deepcopy(board[e])
        for _ in range(a_r):
            A = Rotate(A)
        for _ in range(b_r):
            B = Rotate(B)
        for _ in range(c_r):
            C = Rotate(C)
        for _ in range(d_r):
            D = Rotate(D)
        for _ in range(e_r):
            E = Rotate(E)
        visit = [[[True for _ in range(5)]
                  for _ in range(5)] for _ in range(5)]
        matrix = []
        matrix.append(A)
        matrix.append(B)
        matrix.append(C)
        matrix.append(D)
        matrix.append(E)

        if matrix[0][0][0] == 1:
            tmp = BFS(matrix, 0, 0, 0)
            if tmp != -1:
                res = min(res, tmp)
                flag = True

if flag:
    print(res)
else:
    print(-1)
