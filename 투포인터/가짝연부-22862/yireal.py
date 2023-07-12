import sys
inp = sys.stdin.readline
n,k = map(int,inp().split())
s = list(map(int,inp().split()))
f,r = 0,0
left_k = k
ans = 0
cnt = 0
flag = 0
if n == 1 and s[0] % 2 == 0:
    print(1)
    exit(0)
while True:
    if r >= n : break
    if s[f] % 2 == 0 and s[r] % 2 == 0 and r - f - (k-left_k) >= ans :
        ans = r - f - (k-left_k) + 1
    if f == r :
        r += 1
    if s[f] % 2 == 1:
        f += 1
        if left_k < k:
            left_k += 1
    if s[r] % 2 == 0:
        r += 1
    else:
        if left_k > 0:
            r += 1
            left_k -= 1
        else:
            while s[f] % 2 == 1:
                f += 1
                if left_k < k:
                    left_k += 1
            if s[f] % 2 == 0:
                f += 1
print(ans)
