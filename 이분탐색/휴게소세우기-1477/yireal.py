import sys
inp = sys.stdin.readline
n,m,l = map(int,inp().split())
rs = [0] + list(map(int,inp().split())) + [l]
rs.sort()
f = 1
r = l - 1
ans = 0
while f <= r:
    cnt = 0
    c = (f+r) // 2
    for i in range(1,len(rs)):
        if rs[i] - rs[i-1] > c:
            cnt += (rs[i] - rs[i-1] - 1) // c
    if cnt > m:
        f = c + 1
    else:
        r = c - 1
        ans = c
print(ans)