import sys
inp = sys.stdin.readline
n = int(inp())
a_list = []
b_list = []
c_list = []
d_list = []
ab_comb = []
cd_comb = []
ans = 0
for _ in range(n):
    at,bt,ct,dt = map(int,inp().split())
    a_list.append(at)
    b_list.append(bt)
    c_list.append(ct)
    d_list.append(dt)
for a in a_list:
    for b in b_list:
        ab_comb.append(a+b)
for c in c_list:
    for d in d_list:
        cd_comb.append(c+d)
ab_comb.sort()
cd_comb.sort()
size = n**2
l = 0
r = size - 1
if n == 1:
    if ab_comb[0] + cd_comb[0] == 0:
        print(1)
    else :
        print(0)
    exit()
def clear_top(l):
    cnt = 0
    for i in range(l + 1,size):
        val = ab_comb[i] + cd_comb[0]
        if val == 0 : 
            cnt += 1
        elif val > 0:
            break
    return cnt
def clear_bot(r):
    cnt = 0
    for j in range(r - 1,-1,-1):
        val = ab_comb[-1] + cd_comb[j]
        if val == 0:
            cnt += 1
        elif val < 0:
            break
    return cnt
while True:
    if l == size :
        ans += clear_bot(r)
        break
    if r < 0:
        ans += clear_top(l)
        break
    val = ab_comb[l] + cd_comb[r]
    if val == 0:
        i = l
        j = r
        i_cnt = 0
        j_cnt = 0
        while i < size:
            if ab_comb[i] == ab_comb[l]:
                i_cnt += 1
                i += 1
            else:
                break
        while j >= 0:
            if cd_comb[j] == cd_comb[r]:
                j_cnt += 1
                j -= 1
            else:
                break
        l = i
        r = j
        ans += i_cnt * j_cnt
        if i_cnt == 0 or j_cnt == 0:
            l += 1
    elif val < 0:
        l += 1
    else:
        r -= 1
print(ans)
