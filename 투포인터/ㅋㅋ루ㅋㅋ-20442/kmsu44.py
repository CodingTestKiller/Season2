from collections import deque
import sys
# 9시 40분 시작
n, k = map(int, input().split())
L = list(map(int, input().split()))


even_List = deque()

even_index = 1
for idx, data in enumerate(L):
    if data % 2 == 0:
        even_List.append((idx, even_index))
        even_index += 1


l = (-1, -1)
r = (sys.maxsize, -1)
if even_List:
    l = even_List.popleft()
if even_List:
    r = even_List.pop()


cnt = 0
while l[0] <= r[0]:
