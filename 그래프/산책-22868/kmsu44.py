from collections import deque
n, m = map(int, input().split())
graph = [[0 for _ in range(n+1)] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = b
    graph[b][a] = a

s, e = map(int, input().split())


def BFS(start, end):
    q = deque()
    route = []
    q.append((start, 0, route))
    visit[start] = False
    while q:
        vertex, cnt, route = q.popleft()
        if vertex == end:
            return (cnt, route)
        for v in graph[vertex]:
            if visit[v]:
                visit[v] = False
                route.append(v)
                q.append((v, cnt+1, route.copy()))
                route.pop(-1)
    return (0, 0)


visit = [True for _ in range(n+1)]
visit[0] = False
go_cnt, go_route = BFS(s, e)
visit = [True for _ in range(n+1)]
for visited in go_route:
    visit[visited] = False
visit[0] = False
visit[s] = True
back_cnt, back_route = BFS(e, s)
print(go_cnt + back_cnt)
