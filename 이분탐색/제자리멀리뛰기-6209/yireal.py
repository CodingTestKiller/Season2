import sys
inp = sys.stdin.readline
d,n,m = map(int,inp().split())
rocks = sorted([int(inp()) for _ in range(n)]) + [d]
front,rear,ans = 0,d,0
while front <= rear:
    center,pos,cnt = (front+rear)//2,0,0
    for rock in rocks:
        if rock - pos < center : cnt += 1
        else : pos = rock
    if cnt <= m :
        front = center + 1
        ans = center
    else :
        rear = center - 1
print(ans)