from sys import stdin
input = stdin.readline

inp = [str(x) for x in input().rstrip()]
k_left, k_right = [], []

cnt = 0
for chr in inp:
    if chr == 'K':
        cnt += 1
    else:
        k_left.append(cnt)    

cnt = 0
for chr in inp[::-1]:
    if chr == 'K':
        cnt += 1
    else:
        k_right.append(cnt)
k_right.reverse()

MAX = 0
p1, p2 = 0, len(k_left) - 1
while p1 <= p2:
    MAX = max(MAX, p2 - p1 + 1 + 2 * min(k_left[p1], k_right[p2]))
    if k_left[p1] < k_right[p2]:
        p1 += 1
    else:
        p2 -= 1

print(MAX)