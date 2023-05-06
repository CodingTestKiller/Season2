from collections import defaultdict
n = int(input())
mogi_dict = defaultdict(int)
for i in range(n):
    IN, OUT = map(int, input().split())
    mogi_dict[IN] += 1
    mogi_dict[OUT] -= 1


cnt = 0
max_cnt = 0
s, e = 0, 0
flag = True
for time in sorted(mogi_dict):
    cnt += mogi_dict[time]
    if max_cnt < cnt:
        max_cnt = cnt
        s = time
        flag = True
    elif max_cnt > cnt and flag:
        e = time
        flag = False

print(max_cnt)
print(s, e)
