import sys

str = list(sys.stdin.readline().rstrip())
r_cnt = 0
k_cnt = []
r_pos = []
k_total = 0

for i in range(len(str)):
    if str[i] == 'R':
        r_cnt += 1
        r_pos.append(i)
        k_cnt.append(i - r_cnt + 1)
    else:
        k_total += 1

if r_cnt == 0:
    print(0)
else:
    max_cnt = 0
    s, e = 0, -1
    l = r_pos[s]
    r = r_pos[e]
    while l <= r:
        lk = k_cnt[s]
        rk = k_total - k_cnt[e]
        max_cnt = max(max_cnt, min(lk, rk) * 2 + r_cnt)
        if lk > rk:
            e -= 1
            r_cnt -= 1
        elif lk < rk:
            s += 1
            r_cnt -= 1
        else:
            s += 1
            e -= 1
            r_cnt -= 2
        try:
            l = r_pos[s]
            r = r_pos[e]
        except:
            break
    print(max_cnt)