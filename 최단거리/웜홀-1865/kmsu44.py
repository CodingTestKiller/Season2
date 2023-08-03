T = int(input())


def floyd():
    for k in range(1, N + 1):
        for a in range(1, N + 1):
            for b in range(1, N + 1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
                if a == b and graph[a][b] < 0:
                    return "YES"
    return "NO"


for i in range(T):
    N, M, W = map(int, input().split())
    graph = [[10000 for _ in range(N+1)] for _ in range(N+1)]
    for _ in range(M):
        s, e, t = map(int, input().split())
        graph[s][e] = min(graph[s][e], t)
        graph[e][s] = min(graph[s][e], t)
    for _ in range(W):
        s, e, t = map(int, input().split())
        graph[s][e] = -t
    print(floyd())
