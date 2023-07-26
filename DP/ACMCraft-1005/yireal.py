import sys
from collections import deque
inp = sys.stdin.readline
t = int(inp())
for _ in range(t):
    n,k = map(int,inp().split())
    cost = [0] + list(map(int,inp().split()))
    build = [[] for _ in range(n+1)]
    level = [-1] + [0]*n
    for _ in range(k):
        x,y = map(int,inp().split())
        build[x].append(y)
        level[y] += 1
    w = int(inp())
    dp = [0] * (n+1)
    q = deque()
    for i in range(1,n+1):
        if level[i] == 0:
            q.append(i)
            dp[i] = cost[i]
    while q:
        pos = q.popleft()
        for next in build[pos]:
            level[next] -= 1
            dp[next] = max(dp[next],dp[pos]+cost[next])
            if level[next] == 0:
                q.append(next)
        if level[w] == 0:
            print(dp[w])
            break
