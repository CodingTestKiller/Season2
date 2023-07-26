import sys
inp = sys.stdin.readline
n,k = map(int,inp().split())
way = list(map(int,inp().split()))
dp = [0 for _ in range(n)]
fr = 0
re = 0
ans = 0
cur = 0
top = 0
while True:
    if cur >= k:
        if fr == 0:
            top = 0
        else:
            top = max(top,dp[fr-1])
        dp[re-1] = max(dp[re-1],top+cur-k)
        cur -= way[fr]
        fr += 1
    elif re == n:
        break
    else:
        cur += way[re]
        re += 1
for i in range(n):
    ans = max(ans,dp[i])
print(ans)

