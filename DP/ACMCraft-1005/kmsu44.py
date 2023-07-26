# 1
# 5 10
# 100000 99999 99997 99994 99990
# 4 5
# 3 5
# 3 4
# 2 5
# 2 4
# 2 3
# 1 5
# 1 4
# 1 3
# 1 2
# 4

# 9시 10q분 시작
from collections import defaultdict, deque
import sys

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

    start_list = []
    for i in range(1, N+1):
        if delay_reverse[i]:
            continue
        else:
            start_list.append(i)

    W = int(input())
    dp = [-1 for _ in range(N+1)]
    findcost(W)
    result.append(dp[W])
for i in result:
    print(i)

# 1
# 4 3
# 1 1 1 1
# 1 2
# 3 2
# 1 4
# 4
