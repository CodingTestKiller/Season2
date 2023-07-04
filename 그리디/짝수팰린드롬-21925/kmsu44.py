
n = int(input())
L = list(map(int, input().split()))


def isPalindrome(l, r):
    while l <= r:
        if L[l] == L[r]:
            l = l+1
            r = r-1
        else:
            return False
    return True


cnt = 0
i = 0
while i < n:
    k = i+1
    flag = False
    while k < n:
        if isPalindrome(i, k):
            cnt += 1
            i = k+1
            k = i+1
            flag = True
        else:
            k += 2
    if flag:
        i += 1
    else:
        cnt = -1
        break

print(cnt)
