import sys
from collections import deque

input = sys.stdin.readline

n, h, u = [int(x) for x in input().split()]

matrix = [[x for x in input().strip()] for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]

umbrellas = []


def get_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


for i in range(n):
    for j in range(n):
        if matrix[i][j] == 'S':
            start = (i, j)
            visited[i][j] = h

moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

queue = deque([[start[0], start[1], h, 0, 0]])

while queue:
    x, y, health, umbrella, distance = queue.popleft()
    for move in moves:
        next_x, next_y = x + move[0], y + move[1]

        if next_x < 0 or next_x >= n or next_y < 0 or next_y >= n:
            continue

        next_health = health
        next_umbrella = umbrella

        if matrix[next_x][next_y] == 'E':
            print(distance+1)
            exit()
        elif matrix[next_x][next_y] == 'U':
            next_umbrella = u

        if next_umbrella == 0:
            next_health -= 1
        else:
            next_umbrella -= 1

        if visited[next_x][next_y] < next_health:
            visited[next_x][next_y] = next_health
            queue.append([next_x, next_y, next_health,
                          next_umbrella, distance+1])

print(-1)
