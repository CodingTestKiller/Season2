import sys

def warshallfloyd():
    for k in range(1, N + 1):
        for l in range(1, N + 1):
            for m in range(1, N + 1):
                graph[l][m] = min(graph[l][m], graph[l][k] + graph[k][l])
                if graph[l][m] < 0 and l == m:
                    print("YES")
                    return
    print("NO")

TC = int(sys.stdin.readline())
for _ in range(TC):
    N, M, W = map(int, sys.stdin.readline().split())
    graph = [[1e9]*(N+1) for i in range(N + 1)]
    for j in range(M):
        S, E, T = map(int, sys.stdin.readline().split())
        graph[S][E] = T
        graph[E][S] = T
    for j in range(W):
        S, E, T = map(int, sys.stdin.readline().split())
        graph[S][E] = -T
    warshallfloyd()