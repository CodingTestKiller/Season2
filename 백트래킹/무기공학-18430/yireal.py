import sys
inp = sys.stdin.readline
n,m = map(int,inp().split())
board = [list(map(int,inp().split())) for _ in range(n)]
used = [[0]*m for _ in range(n)]
offset = [[(1,0),(0,1)],[(0,-1),(1,0)],[(-1,0),(0,1)],[(-1,0),(0,-1)]]
max_val = 0
def counter(center,left,right):
    return board[center[1]][center[0]] * 2 + board[left[1]][left[0]] + board[right[1]][right[0]]
def check_range(x,y,x1,y1,x2,y2):
    if x1 < 0 or y1 < 0 or x2 < 0 or y2 < 0 or x1 >= m or x2 >= m or y1 >= n or y2 >= n :
        return False
    if used[y][x] == 1 or used[y1][x1] == 1 or used[y2][x2] == 1:
        return False 
    return True
def find_next(pos):
    x = pos[0]
    y = pos[1]
    x += 1
    if x >= m:
        x = 0
        y += 1
    if y >= n:
        return (-1,-1)
    return (x,y)
def back_tracking(pos,sum):
    global max_val
    x = pos[0]
    y = pos[1]
    if x == -1 and y == -1:    
        max_val = max(max_val,sum)
        return
    tmp = find_next((x,y))
    if used[y][x] == 0:
        for shape in offset:
            n1x = shape[0][0] + x
            n1y = shape[0][1] + y
            n2x = shape[1][0] + x
            n2y = shape[1][1] + y
            if check_range(x,y,n1x,n1y,n2x,n2y) == True:
                used[y][x] = 1
                used[n1y][n1x] = 1
                used[n2y][n2x] = 1
                val = counter((x,y),(n1x,n1y),(n2x,n2y))
                back_tracking(tmp,sum+val)
                used[y][x] = 0
                used[n1y][n1x] = 0
                used[n2y][n2x] = 0
    back_tracking(tmp,sum)
back_tracking((0,0),0)
print(max_val)
    
        
        