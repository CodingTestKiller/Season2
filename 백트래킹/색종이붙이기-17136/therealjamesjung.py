from sys import stdin
from collections import deque

input = stdin.readline


def validate(board, x, y, k):
    for i in range(x, x+k):
        for j in range(y, y+k):
            if i < 0 or i >= 10 or j < 0 or j >= 10 or board[i][j] == 0:
                return False
    return True


def put_paper(board, x, y, k):
    for i in range(x, x+k):
        for j in range(y, y+k):
            board[i][j] = 0


def remove_paper(board, x, y, k):
    for i in range(x, x+k):
        for j in range(y, y+k):
            board[i][j] = 1


board = [[int(x) for x in input().split()] for _ in range(10)]

papers = [0, 5, 5, 5, 5, 5]
min_cnt = 26

targets = deque()

for i in range(10):
    for j in range(10):
        if board[i][j] == 1:
            targets.append((i, j))


def solve(cnt):
    global min_cnt

    if cnt >= min_cnt:
        return

    if not targets:
        min_cnt = min(min_cnt, cnt)
        return

    current_x, current_y = targets.popleft()

    if board[current_x][current_y] == 0:
        solve(cnt)
        targets.appendleft((current_x, current_y))
        return

    for k in range(5, 0, -1):
        if validate(board, current_x, current_y, k):
            if papers[k] == 0:
                continue
            papers[k] -= 1
            put_paper(board, current_x, current_y, k)
            solve(cnt+1)
            remove_paper(board, current_x, current_y, k)
            papers[k] += 1

    targets.appendleft((current_x, current_y))


solve(0)
print(min_cnt if min_cnt != 26 else -1)
