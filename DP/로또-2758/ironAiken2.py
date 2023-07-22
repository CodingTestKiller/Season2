from sys import stdin
input = stdin.readline
from copy import deepcopy

dp = [[0]*2001 for i in range(11)]
dp[0] = [1]*2001
for i in range(1, 11):
    for j in range(1, 2001):
        dp[i][j] = dp[i][j-1]+dp[i-1][j//2]

t = int(input())
for _ in range(t):
    n, m = [int(x) for x in input().split()]
    print(dp[n][m])