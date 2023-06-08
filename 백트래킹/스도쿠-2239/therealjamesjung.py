from sys import stdin
from collections import deque

input = stdin.readline

board = [[int(x) for x in input().strip()] for _ in range(9)]

targets = deque()

for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            targets.append((i, j))


def v_check(board, x, y):
    for i in range(9):
        if i == x:
            continue
        if board[i][y] == board[x][y]:
            return False
    return True


def h_check(board, x, y):
    for i in range(9):
        if i == y:
            continue
        if board[x][i] == board[x][y]:
            return False
    return True


def box_check(board, x, y):
    for i in range(3):
        for j in range(3):
            if (x//3)*3+i == x and (y//3)*3+j == y:
                continue
            if board[(x//3)*3+i][(y//3)*3+j] == board[x][y]:
                return False
    return True


def validate(board, x, y, k):
    board[x][y] = k
    result = v_check(board, x, y) and h_check(
        board, x, y) and box_check(board, x, y)
    board[x][y] = 0
    return result


def solve():
    if not targets:
        for row in board:
            print(''.join(map(str, row)))
        exit()

    current_x, current_y = targets.popleft()

    for i in range(1, 10):
        if validate(board, current_x, current_y, i):
            board[current_x][current_y] = i
            solve()
            board[current_x][current_y] = 0

    targets.appendleft((current_x, current_y))


solve()
