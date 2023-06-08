import sys
inp = sys.stdin.readline
sys.setrecursionlimit(10**5)
sticker = [list(map(int,inp().split())) for _ in range(10)]
store = [5,5,5,5,5]
total = 25
def check(x,y,offset):
    for i in range(y,y+offset+1):
        for j in range(x,x+offset+1):
            if sticker[i][j] != 1 : return False
    return True
def back_tracking(x,y,cnt):
    global store,total
    if y >= 10:
        total = min(total,cnt)
        return
    if x >= 10:
        back_tracking(0,y+1,cnt)
        return
    if sticker[y][x] == 1:
        for k in range(5):
            if store[k] == 0 :   continue
            if x+k >= 10 or y+k >= 10 : continue
            if not check(x,y,k): break
            for i in range(y,y+k+1):
                for j in range(x,x+k+1):
                    sticker[i][j] = 0
            store[k] -= 1
            back_tracking(x+k+1,y,cnt+1)
            store[k] += 1
            for i in range(y,y+k+1):
                for j in range(x,x+k+1):
                    sticker[i][j] = 1
    else:
        back_tracking(x+1,y,cnt)
back_tracking(0,0,0)
print(-1 if total == 25 else total)