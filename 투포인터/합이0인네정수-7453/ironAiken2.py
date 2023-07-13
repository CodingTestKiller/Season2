from sys import stdin
from itertools import product
input = stdin.readline

n = int(input())
a, b, c, d, = [], [], [] ,[]
for _ in range(n):
    cmd = [int(x) for x in input().split()]
    
    a.append(cmd[0])
    b.append(cmd[1])
    c.append(cmd[2])
    d.append(cmd[3])

ab = []
cd = []
for n1 in a:
    for n2 in b:
        ab.append(n1 + n2)
for n1 in c:
    for n2 in d:
        cd.append(n1 + n2)

ab.sort()
cd.sort()

std = len(ab)
abcd = ab + cd

p1, p2 = 0, len(abcd) - 1
ans = 0
flag = 0

while p1 < p2 and p1 < std and p2 >= std:
    if abcd[p1] + abcd[p2] == 0:
        pp1, pp2 = p1 + 1, p2 - 1
        cnt1, cnt2 = 1, 1
        while pp1 < std and abcd[p1] == abcd[pp1]:
            cnt1 += 1
            pp1 += 1
        while pp2 >= std and abcd[p2] == abcd[pp2]:
            cnt2 += 1
            pp2 -= 1
        ans += cnt1 * cnt2
        p1, p2 = pp1, pp2
    else:
        if abcd[p1] + abcd[p2] > 0:
            p2 -= 1
        else:
            p1 += 1

print(ans)