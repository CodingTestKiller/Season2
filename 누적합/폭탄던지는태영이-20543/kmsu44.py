import sys
input = sys.stdin.readline


def findBomb(dp, x1, y1, x2, y2):
    x1, y1 = max(x1, 1), max(y1, 1)
    return dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1]


N, M = map(int, input().split())


board = [[0 for i in range(
    N+1)]] + [[0] + list(map(lambda x: -int(x), input().split())) for i in range(N)]
if M == 1:
    for i in board[1:]:
        print(*i[1:])
    exit()
ret = [[0 for _ in range(N+1)] for _ in range(N+1)]
dp = [[0 for _ in range(N+1)] for _ in range(N+1)]

for i in range(1, N-M+2):
    for j in range(1, N-M+2):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]
        ret[i][j] = board[i][j] - findBomb(dp, i-M+1, j-M+1, i, j)
        dp[i][j] += ret[i][j]

for i in range(1, N+1):
    for j in range(1, N+1):
        x, y = i - M//2, j - M//2
        print((0 if x < 1 or y < 1 else ret[x][y]), end=' ')
    print()
