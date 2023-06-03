# 10시 30분 시작
L = [list(input()) for _ in range(9)]
zero_cnt = 0
for i in range(9):
    for j in range(9):
        if L[i][j] == '0':
            zero_cnt += 1
squre = {0: 0, 1: 0, 2: 0, 3: 3, 4: 3, 5: 3, 6: 6, 7: 6, 8: 6}


def check(x, y, num):
    # row 확인
    for i in range(9):
        if i == y:
            continue
        if int(L[x][i]) == num:
            return False
    for i in range(9):
        if i == x:
            continue
        if int(L[i][y]) == num:
            return False

    a, b = squre[x], squre[y]
    # 3 * 3 확인
    for i in range(3):
        for j in range(3):
            if i == x and j == y:
                continue
            if int(L[a+i][b+j]) == num:
                return False
    return True


def DFS(x, y, cnt):
    if y == 9:
        x += 1
        y = 0

    if zero_cnt == cnt:
        for i in L:
            for j in i:
                print(j, end='')
            print()

        exit()
    if x == 9:
        return
    if L[x][y] == '0':
        for i in range(1, 10):
            if check(x, y, i):
                L[x][y] = str(i)
                DFS(x, y+1, cnt + 1)
                L[x][y] = '0'
    else:
        DFS(x, y+1, cnt)


DFS(0, 0, 0)
