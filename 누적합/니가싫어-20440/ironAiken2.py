from sys import stdin
input = stdin.readline

n = int(input())
mos = {}
for _ in range(n):
    s, e = [int(x) for x in input().split()]

    mos[s] = mos.get(s, 0) + 1
    mos[e] = mos.get(e, 0) - 1

mos = dict(sorted(mos.items()))

_max = 0
_sum = 0
s, e = 0, 0
flag = False

for key in mos:
    if mos[key] < 0 and flag == True:
        e = key
        flag = False
    _sum += mos[key]
    if _max < _sum:
        _max = _sum
        s = key
        flag = True

print(_max)
print(s, e)
