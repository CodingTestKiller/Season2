import sys

dp = [[0]*2001 for _ in range(11)]
for i in range(2001):
    dp[0][i] = 1

for i in range(1, 11):
    for j in range(1, 2001):
        dp[i][j] = dp[i][j-1] + dp[i-1][j//2]

T = int(sys.stdin.readline())
for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    print(dp[N][M])
