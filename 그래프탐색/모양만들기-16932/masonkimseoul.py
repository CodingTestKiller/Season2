import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited_node = deque()
visited = [[0] * M for _ in range(N)]
answer = 0

def BFS(a, b):
    global answer
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    q = deque([[a, b]])
    while q:
        node = q.popleft()
        if visited[node[0]][node[1]] == 1:
            continue
        visited[node[0]][node[1]] = 1
        visited_node.append(node)
        answer += 1
        for k in range(4):
            nx = node[0] + dx[k]
            ny = node[1] + dy[k]
            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                    q.append([nx, ny])

for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            graph[i][j] = 1
            tmp = answer
            answer = 0
            BFS(i, j)
            answer = max(tmp, answer)
            graph[i][j] = 0
            while visited_node:
                node = visited_node.pop()
                visited[node[0]][node[1]] = 0

print(answer)