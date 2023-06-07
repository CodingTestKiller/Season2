import sys
inp = sys.stdin.readline
NUM = 9

def check_row(y,num):
    for x in range(NUM):
        if board[y][x] == num:
            return False
    return True
def check_col(x,num):
    for y in range(NUM):
        if board[y][x] == num:
            return False
    return True
def check_box(x,y,num):
    nx = (x//3) * 3
    ny = (y//3) * 3
    for i in range(3):
        for j in range(3):
            if board[ny+i][nx+j] == num :
                return False

    return True

def dfs(level):
    if level == len(index):
        for y in range(NUM):
            for x in range(NUM):
                print(board[y][x],end = '')
            print()
        exit()
    nx,ny = index[level]
    for num in range(1,10):
        if check_row(ny,num) and check_col(nx,num) and check_box(nx,ny,num):
            board[ny][nx] = num
            dfs(level + 1)
            board[ny][nx] = 0  
board = []
index = []		
for y in range(9):
    board.append(list(map(int, inp().rstrip())))
    for x in range(9):
        if board[y][x] == 0:
            index.append((x, y))

dfs(0)
