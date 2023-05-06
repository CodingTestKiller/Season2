import sys
inp = sys.stdin.readline
cnt = 0
en = []
ex = []
ans = [0] * 2
n = int(inp())
for _ in range(n):
    t1,t2 = map(int,inp().split())
    en.append(t1)
    ex.append(t2)
en.sort()
ex.sort()
max_cnt = 0
ex_cnt = 0
en_cnt = 0
flag = 0
while en_cnt < n:
    if cnt > max_cnt:
        max_cnt = cnt
        flag = 1
    if en[en_cnt] == ex[ex_cnt]:
        en_cnt += 1
        ex_cnt += 1
    elif en[en_cnt] > ex[ex_cnt]:
        if cnt == max_cnt and flag == 1:
            ans[1] = ex[ex_cnt]
        cnt -= 1
        flag = 0
        ex_cnt += 1
    else :
        if cnt == max_cnt :
            ans[0] = en[en_cnt]
        cnt += 1
        en_cnt += 1
if  ans[1] <= ans[0]:
    ans[1] = ex[ex_cnt]
print(max(max_cnt,cnt))
print(*ans)
    
