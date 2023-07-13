from sys import stdin

input = stdin.readline

string = input().strip()

r_cnt, l, r = 0, 0, 0
flag = True

for i, c in enumerate(string):
    if c == 'R':
        r_cnt += 1
        if flag:
            l = i
            r = i
            flag = False

result = r_cnt
tmp = r_cnt
k_cnt = len(string) - r_cnt

while tmp > 1:
    if string[r] == 'R':
        tmp -= 1
    r += 1

while True:
    r += 1
    l -= 1
    if r >= len(string) or l < 0:
        break
    if string[r] == 'K' and string[l] == 'K':
        result += 2

l, r = 0, len(string) - 1

tmp = 0

while l < r and r_cnt:
    while string[l] == 'R' and l < r and r_cnt:
        l += 1
        r_cnt -= 1
    while string[r] == 'R' and l < r and r_cnt:
        r -= 1
        r_cnt -= 1

    while string[l] == 'K' and string[r] == 'K' and l < r and r_cnt:
        l += 1
        r -= 1
        tmp += 2

    result = max(result, tmp + r_cnt)

print(result)
