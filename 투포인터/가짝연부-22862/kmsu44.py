# 12시 55분 시작
from collections import deque

n, k = map(int, input().split())
L = list(map(int, input().split()))

left = 0
right = 0
res = 0
result = 0
while right < n:

    if L[right] % 2 == 0:
        res += 1
    else:
        # 지울 수 있는 수가 남은 경우
        if k > 0:
            k -= 1
        # 지울 수 있는 수가 없는 경우
        else:
            k -= 1
            while L[left] % 2 == 0 and left < right:
                res -= 1
                left += 1
            while L[left] % 2 != 0 and left < right:
                k += 1
                left += 1
    # print('left', L[left], 'right', L[right], end='')
    # print('result', result, 'res', res, 'k', k)
    right += 1
    result = max(result, res)


print(result)
