from sys import stdin
input = stdin.readline

sdoku = [[int(x) for x in input().rstrip()] for _ in range(9)]


def check(x: int, y: int, n: int) -> bool:
    for i in range(9):
        if sdoku[x][i] == n or sdoku[i][y] == n:
            return False
    for i in range(3):
        for j in range(3):
            if sdoku[(x//3)*3+i][(y//3)*3+j] == n:
                return False
    return True


def dfs():
    for i in range(9):
        for j in range(9):
            if sdoku[i][j] == 0:
                for n in range(1, 10):
                    if check(i, j, n):
                        sdoku[i][j] = n
                        dfs()
                        sdoku[i][j] = 0
                return
    for i in range(9):
        for j in range(9):
            print(sdoku[i][j], end='')
        print()

    exit()


dfs()
