import sys

board = [list(map(int, sys.stdin.readline().split())) for _ in range(10)]
paper = [0, 0, 0, 0, 0]

answer = 26
def DFS(x, y, cnt):
    global answer
    if x >= 10:
        answer = min(answer, cnt)
        return
    if y >= 10:
        DFS(x + 1, 0, cnt)
        return
    if board[x][y] == 1:
        for i in range(5):
            if paper[i] >= 5:
                continue
            if x + i < 0 or x + i >= 10 or y + i < 0 or y + i >= 10:
                continue

            check = True

            for nx in range(x, x + i + 1):
                for ny in range(y, y + i + 1):
                    if board[nx][ny] == 0:
                        check = False
                        break
                if not check:
                    break
            if check:
                for nx in range(x, x + i + 1):
                    for ny in range(y, y + i + 1):
                        board[nx][ny] = 0

                paper[i] += 1
                DFS(x, y + i + 1, cnt + 1)
                paper[i] -= 1
                for nx in range(x, x + i + 1):
                    for ny in range(y, y + i + 1):
                        board[nx][ny] = 1
    else:
        DFS(x, y + 1, cnt)

DFS(0, 0, 0)
if answer == 26:
    answer = -1
print(answer)