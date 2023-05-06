from sys import stdin
input = stdin.readline

n, m = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]

sum = 0
remain = {}

for num in arr:
    sum += num

    try:
        remain[sum % m] += 1
    except KeyError:
        remain[sum % m] = 1

ans = remain[0] if 0 in remain else 0

for key in remain:
    ans += remain[key] * (remain[key] - 1) // 2

print(ans)
