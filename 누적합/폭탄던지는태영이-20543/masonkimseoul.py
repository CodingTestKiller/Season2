import sys
N, M = map(int, sys.stdin.readline().split())
field = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
bombs = [[0 for i in range(N)] for j in range(N)]
point = int(M/2)

if M == 1:
    for i in range(N):
        tmp = []
        for j in range(N):
            tmp.append((-1)*field[i][j])
        print(*tmp)
else:

    for i in range(N):
        for j in range(N):
            x1, y1, x2, y2 = N - 1, N - 1, 0, 0
            if i + point < N:
                x1 = i + point
            if j + point < N:
                y1 = j + point
            if i - point >= 1:
                x2 = i - point - 1
            if j - point >= 1:
                y2 = j - point - 1

            if x1 >= N or y1 >= N:
                continue

            bombs[x1][y1] = bombs[x1-1][y1] + bombs[x1][y1-1] - bombs[x1-1][y1-1]
            prefix = (-1)*(bombs[x1][y1] - bombs[x1][y2] - bombs[x2][y1] + bombs[x2][y2] + field[i][j])
            bombs[x1][y1] += prefix

    for i in range(N):
        tmp=[]
        for j in range(N):
            x, y = i - 1, j - 1
            if i - 1 < 0:
                x = 0
            if j - 1 < 0:
                y = 0
            tmp.append(bombs[i][j] - bombs[x][j] - bombs[i][y] + bombs[x][y])
        print(*tmp)
