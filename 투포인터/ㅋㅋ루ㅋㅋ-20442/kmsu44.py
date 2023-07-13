L = list(map(str, input().strip()))

k_count = 0
r_count = 0
for i in L:
    if i == 'K':
        k_count += 1
    else:
        r_count += 1

# k가 0개 의 짝일 때
res = r_count
tmp_rcount = r_count
k_cnt = 0
left = 0
right = len(L)-1
# K가 use_k개 사용
for use_k in range(1, k_count//2+1):
    while 0 <= left < len(L):
        if L[left] == 'K':
            left += 1
            break
        elif L[left] == 'R':
            tmp_rcount -= 1
        left += 1
    while 0 <= right < len(L):
        if L[right] == 'K':
            right -= 1
            break
        elif L[right] == 'R':
            tmp_rcount -= 1
        right -= 1

    if tmp_rcount > 0:
        res = max(res, use_k*2 + tmp_rcount)
    else:
        continue
print(res)
