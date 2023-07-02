N = int(input())
arr = [['' for _ in range(N)] for _ in range(7)]


def solution(depth, left, right):
    if depth == 7:
        return
    mid = (left + right)//2

    for i in range(left, mid):
        arr[depth][i] = 'A'
    for i in range(mid, right):
        arr[depth][i] = 'B'

    solution(depth+1, left, mid)
    solution(depth+1, mid, right)


solution(0, 0, N)
for i in range(7):
    if 'A' not in arr[i]:
        arr[i][0] = 'A'
    print(''.join(arr[i]))
