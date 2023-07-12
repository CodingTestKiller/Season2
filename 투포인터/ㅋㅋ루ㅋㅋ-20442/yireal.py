import sys
inp = sys.stdin.readline
jam = list(inp().rstrip())
r_cnt = 0
k_cnt = []
r_pos = []
total_k = 0
for i in range(len(jam)):
    if jam[i] == 'R':
        r_cnt += 1
        r_pos.append(i)
        k_cnt.append(i - r_cnt + 1)
    else:
        total_k += 1
if r_cnt == 0:
    print(0)
    exit()

big_kkrkk = 0
l,r = 0,-1

left = r_pos[l]
right = r_pos[r]
while left <= right:
    l_k = k_cnt[l]
    r_k = total_k - k_cnt[r]
    big_kkrkk = max(big_kkrkk, min(l_k,r_k)*2 + r_cnt)
    if l_k > r_k:
        r -= 1
        r_cnt -= 1
    elif l_k < r_k:
        l += 1
        r_cnt -= 1
    else:
        l += 1
        r -= 1
        r_cnt -= 2

    try :
        left = r_pos[l]
        right = r_pos[r]
    except:
        break
print(big_kkrkk)