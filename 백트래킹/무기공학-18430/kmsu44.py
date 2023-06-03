# 1시 10분 시작

n, m = map(int, input().split())
L = [list(map(int, input().split())) for _ in range(n)]
if n == m == 1:
    print(0)
    exit()

shape = [
    # ㄱ
    [[0, 0], [0, -1], [1, 0]],
    # 90
    [[0, 0], [-1, 0], [0, -1]],
    # 180
    [[0, 0], [-1, 0], [0, 1]],
    # 270
    [[0, 0], [0, 1], [1, 0]]
]


def boomerang(x, y, k):
    result = L[x][y]
    for sx, sy in shape[k]:
        if 0 <= sx+x < n and 0 <= sy+y < m:
            result += L[sx+x][sy+y]
    return result


def check(x, y, k):
    for sx, sy in shape[k]:
        if 0 <= sx+x < n and 0 <= sy+y < m and visit[sx+x][sy+y]:
            continue
        else:
            return False
    return True


res = 0


def DFS(x, y, cnt):
    global res
    if y == m:
        x += 1
        y = 0
    if x == n:
        res = max(res, cnt)

        return

    if visit[x][y]:
        for i in range(4):
            if check(x, y, i):
                for sx, sy in shape[i]:
                    if 0 <= sx+x < n and 0 <= sy+y < m:
                        visit[sx+x][sy+y] = False
                DFS(x, y+1, cnt+boomerang(x, y, i))
                for sx, sy in shape[i]:
                    if 0 <= sx+x < n and 0 <= sy+y < m:
                        visit[sx+x][sy+y] = True
        DFS(x, y+1, cnt)
    else:
        DFS(x, y+1, cnt)


visit = [[True for _ in range(m)] for _ in range(n)]

DFS(0, 0, 0)

print(res)
