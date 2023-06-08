from sys import stdin

input = stdin.readline

n, m = [int(x) for x in input().split()]

board = [[int(x) for x in input().split()] for _ in range(n)]
visited = [[0] * m for _ in range(n)]


def get_boomerang(board, x, y):
    result = []

    cases = [
        [(0, 1), (1, 0)],
        [(1, 0), (0, -1)],
        [(0, -1), (-1, 0)],
        [(-1, 0), (0, 1)]
    ]

    for (x1, y1), (x2, y2) in cases:
        if 0 <= x+x1 < n and 0 <= y+y1 < m and 0 <= x+x2 < n and 0 <= y+y2 < m:
            result.append(((x+x1, y+y1), (x+x2, y+y2),
                          ((board[x][y]*2) + board[x+x1][y+y1] + board[x+x2][y+y2])))

    return result


# print(get_boomerang(board, 0, 0))

max_boomerang = 0


def dfs(board, x, y, boomerang, visited):
    global max_boomerang

    if y == m:
        x += 1
        y = 0
    if x == n:
        max_boomerang = max(max_boomerang, boomerang)
        return

    for p1, p2, b in get_boomerang(board, x, y):
        if visited[p1[0]][p1[1]] or visited[p2[0]][p2[1]] or visited[x][y]:
            continue
        visited[x][y] = 1
        visited[p1[0]][p1[1]] = 1
        visited[p2[0]][p2[1]] = 1
        dfs(board, x, y+1, boomerang+b, visited)
        visited[x][y] = 0
        visited[p1[0]][p1[1]] = 0
        visited[p2[0]][p2[1]] = 0

    dfs(board, x, y+1, boomerang, visited)


for i in range(n):
    for j in range(m):
        dfs(board, i, j-1, 0, visited)

print(max_boomerang)
