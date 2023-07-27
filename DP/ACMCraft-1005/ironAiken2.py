from sys import stdin, setrecursionlimit
setrecursionlimit(10**9)
input = stdin.readline

def cal_delay(now: int) -> int:
    if not tree[now] : return delay[now]
    if total_delay[now] != -1: return total_delay[now]

    for build in tree[now]:
        total_delay[now] = max(total_delay[now], cal_delay(build))
    total_delay[now] += delay[now]
    return total_delay[now]

t = int(input())
for _ in range(t):
    n, k = [int(x) for x in input().split()]
    delay = [0] + [int(x) for x in input().split()]
    tree = [[] for _ in range(n+1)]
    total_delay = [-1] * (n+1)
    for _ in range(k):
        s, e = [int(x) for x in input().split()]
        tree[e].append(s)
    goal = int(input())

    print(cal_delay(goal))
