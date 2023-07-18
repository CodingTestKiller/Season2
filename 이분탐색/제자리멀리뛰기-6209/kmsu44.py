# 9시 30분 시작
d, n, m = map(int, input().split())
dist = []
for _ in range(n):
    dist.append(int(input()))

dist.sort()
l, r = 0, d
ans = 0
while l <= r:
    mid = (l+r) // 2
    pos = 0
    remove_cnt = 0
    m_distance = d
    for i in dist:
        if i - pos >= mid:
            m_distance = min(m_distance, i-pos)
            pos = i
        else:
            remove_cnt += 1
    m_distance = min(m_distance, d-pos)

    if remove_cnt <= m:
        ans = max(ans, m_distance)
        l = mid + 1
    else:
        r = mid - 1
print(ans)
