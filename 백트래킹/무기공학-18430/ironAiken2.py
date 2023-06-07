from sys import stdin
input = stdin.readline

n, m = [int(x) for x in input().split()]
board = [[int(x) for x in input().split()] for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
moves = [[[0, 1], [-1, 0]], [[0, 1], [1, 0]],
         [[1, 0], [0, -1]], [[-1, 0], [0, -1]]]
ans = 0


def check(x: int, y: int, move: list) -> bool:
    global visited

    for dx, dy in move:
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            return False
        if visited[nx][ny]:
            return False

    return True


def calc(x: int, y: int, move: list) -> int:
    global board

    sum = 0
    for dx, dy in move:
        nx, ny = x + dx, y + dy
        sum += board[nx][ny]

    sum += board[x][y] * 2

    return sum


def dfs(x: int, y: int, sum: int) -> None:
    global ans

    if y == m:
        x += 1
        y = 0
    if x == n:
        ans = max(ans, sum)
        return

    if visited[x][y] == False:
        for i in range(4):
            if check(x, y, moves[i]):
                for dx, dy in moves[i]:
                    nx, ny = x + dx, y + dy
                    visited[nx][ny] = True
                visited[x][y] = True
                dfs(x, y + 1, sum + calc(x, y, moves[i]))
                visited[x][y] = False
                for dx, dy in moves[i]:
                    nx, ny = x + dx, y + dy
                    visited[nx][ny] = False

    dfs(x, y + 1, sum)


dfs(0, 0, 0)
print(ans)
