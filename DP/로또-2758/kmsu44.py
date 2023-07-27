# 5시 57분 시작
import sys
input = sys.stdin.readline
N = 10
M = 2000
dp = [[0 for _ in range(M+1)] for _ in range(N+1)]

for i in range(1, M+1):
    dp[1][i] = i


for i in range(2, N+1):
    tmp_i = i
    for j in range(1, M+1):
        dp[i][j] = dp[i][j-1] + dp[i-1][j//2]


T = int(input())
for i in range(T):
    N, M = map(int, input().split())
    print(dp[N][M])
