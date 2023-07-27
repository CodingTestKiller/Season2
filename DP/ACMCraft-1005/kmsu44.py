from collections import defaultdict

T = int(input())
result = []


def findcost(W):
    if dp[W] != -1:
        return dp[W]
    for i in delay_reverse[W]:
        dp[W] = max(dp[W], findcost(i) + rule[W-1])
    if dp[W] == -1:
        dp[W] = rule[W-1]
    return dp[W]


for _ in range(T):
    N, K = map(int, input().split())
    rule = list(map(int, input().split()))
    delay_reverse = defaultdict(list)
    for _ in range(K):
        a, b = map(int, input().split())
        delay_reverse[b].append(a)

    W = int(input())
    dp = [-1 for _ in range(N+1)]
    findcost(W)
    result.append(dp[W])
for i in result:
    print(i)
