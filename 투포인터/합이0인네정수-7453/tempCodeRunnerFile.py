import sys
inp = sys.stdin.readline
n = int(inp())
a_list = []
b_list = []
c_list = []
d_list = []
l_comb = []
r_comb = []
ans = 0
for _ in range(n):
    at,bt,ct,dt = map(int,inp().split())
    a_list.append(at)
    b_list.append(bt)
    c_list.append(ct)
    d_list.append(dt)
for a in a_list:
    for b in b_list:
        l_comb.append(a+b)
for c in c_list:
    for d in d_list:
        r_comb.append(c+d)
l_comb.sort()
r_comb.sort()
l_size = len(l_comb)
r_size = len(r_comb)
l = 0
r = r_size - 1
while True:
    if l == l_size or r < 0:
        break
    if l_comb[l] + r_comb[r] == 0:
        ans += 1
        if l_comb[l] == r_comb[r]:
            ans += 1
        l += 1
    elif l_comb[l] + r_comb[r] < 0:
        l += 1
    else:
        r -= 1
while l < l_size:
    if l_comb[l] + r_comb[0] == 0:
        ans += 1
        if l_comb[l] == r_comb[0]:
            ans += 1
    if l_comb[l] + r_comb[0] > 0:
        break
    l += 1
while r >= 0:
    if l_comb[-1] + r_comb[r] == 0:
        ans += 1
        if l_comb[-1] == r_comb[r]:
            ans += 1
    if l_comb[-1] + r_comb[r] < 0:
        break
    r -= 1
print(ans)
