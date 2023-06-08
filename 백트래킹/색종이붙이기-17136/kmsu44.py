import copy
from collections import deque
L = [list(map(int, input().split())) for _ in range(10)]
Remove_cnt = 0
q = deque()
for i in range(10):
    for j in range(10):
        if L[i][j] == 1:
            Remove_cnt += 1
            q.append((i, j))


shape_cnt = {0: 0, 1: 5, 2: 5, 3: 5, 4: 5, 5: 5}


def checknxn(x, y, n):
    if shape_cnt[n] <= 0:
        return False
    for i in range(n):
        for j in range(n):
            if 0 <= i + x < 10 and 0 <= j + y < 10:
                if L[i+x][j+y] == 0:
                    return False
            else:
                return False
    return True


def visit(x, y, n):
    for i in range(n):
        for j in range(n):
            if 0 <= i + x < 10 and 0 <= j + y < 10:
                L[i+x][j+y] = 0


def remove(x, y, n):
    for i in range(n):
        for j in range(n):
            if 0 <= i + x < 10 and 0 <= j + y < 10:
                L[i+x][j+y] = 1


res = 1000


def DFS(x, y, remove_cnt, cnt):
    global res
    global Remove_cnt
    if y == 10:
        x = x+1
        y = 0
    if remove_cnt == Remove_cnt:
        res = min(res, cnt)
    if x == 10:
        return
    if cnt >= res:
        return
    if L[x][y] == 1:
        for i in range(1, 6):
            if checknxn(x, y, i):
                visit(x, y, i)
                R = (i) * (i)
                shape_cnt[i] -= 1
                DFS(x, y+1, remove_cnt + R, cnt+1)
                shape_cnt[i] += 1
                remove(x, y, i)
    else:
        DFS(x, y+1, remove_cnt, cnt)


DFS(0, 0, 0, 0)
if res == 1000:
    print(-1)
else:
    print(res)
