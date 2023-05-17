from sys import stdin
input = stdin.readline
from collections import deque

n, m = [int(x) for x in input().split()]
nodes = [[] for _ in range(n+1)]
visit = [False for _ in range(n+1)]
for _ in range(m):
    a, b = [int(x) for x in input().split()]
    nodes[a].append(b)
    nodes[b].append(a)

s, e = [int(x) for x in input().split()]

for node in nodes:
    #이거 정렬 하나때문에 세시간 씀
    node.sort()

def bfs(x: int, e: int) -> list:
    q = deque()
    q.append((x, []))
    visit[x] = True

    while q:
        n, log = q.popleft()
        # print(n, log)
        log.append(n)

        if n == e:
            return log

        for node in nodes[n]:
            if visit[node] == False:
                q.append((node, log[:]))
                visit[node] = True

    return []

result = bfs(s, e)
ans = 0 + len(result) - 1
visit = [False for _ in range(n+1)]

for node in result:
    visit[node] = True if node != s and node!= e else False
result = bfs(s, e)
ans += len(result) - 1

print(ans)