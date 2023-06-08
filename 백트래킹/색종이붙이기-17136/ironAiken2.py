from sys import stdin
input = stdin.readline

board = [[int(x) for x in input().split()] for _ in range(10)]
used_paper = [0 for _ in range(5)]
ans = 101


def check(x: int, y: int, i: int) -> bool:
    for ii in range(x, x + i + 1):
        for jj in range(y, y + i + 1):
            if board[ii][jj] == 0:
                return False
    return True


def dfs(x: int, y: int, sum: int) -> None:
    global ans

    if y >= 10:
        ans = min(ans, sum)
        return
    if x >= 10:
        dfs(0, y + 1, sum)
        return

    if board[x][y] == 1:
        for i in range(5):
            if used_paper[i] == 5:
                continue
            if x + i >= 10 or y + i >= 10:
                continue

            if check(x, y, i):
                for ii in range(x, x + i + 1):
                    for jj in range(y, y + i + 1):
                        board[ii][jj] = 0

                used_paper[i] += 1
                dfs(x + i + 1, y, sum + 1)
                used_paper[i] -= 1

                for ii in range(x, x + i + 1):
                    for jj in range(y, y + i + 1):
                        board[ii][jj] = 1

    else:
        dfs(x + 1, y, sum)


dfs(0, 0, 0)
print(ans) if ans != 101 else print(-1)
