import sys
sys.setrecursionlimit(111111)

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    teams = [0] + list(map(int, sys.stdin.readline().split()))
    visited = [0] * (N + 1)
    checked = [0] * (N + 1)
    answer = N

    def DFS(_now):
        global answer
        visited[_now] = 1
        _next = teams[_now]
        if visited[_next] == 0:
            DFS(_next)
        else:
            if checked[_next] == 0:
                answer -= 1
                while _next != _now:
                    _next = teams[_next]
                    answer -= 1
        checked[_now] = 1

    for i in range(1, N + 1):
        if visited[i] == 0:
            DFS(i)
    print(answer)