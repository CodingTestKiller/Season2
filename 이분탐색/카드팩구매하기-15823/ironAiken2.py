from sys import stdin
input = stdin.readline

n, m = [int(x) for x in input().split()]
cards = [int(x) for x in input().split()]

# 카드팩 최소, 최대 크기
lo = 1
hi = n//m

def count_m(mid):
    cnt = 0
    move = 0

    while mid + move <= n:
        visited = dict()
        for i in range(move, move + mid):
            if cards[i] not in visited:
                visited[cards[i]] = i
            else:
                move = visited[cards[i]] + 1
                break
        else:
            cnt = cnt + 1
            move = move + mid

    return cnt

def my_bisect(lo, hi):
    answer = 0
    while lo <= hi:
        mid = (lo + hi) // 2
        cnt = count_m(mid)
        if cnt >= m:
            answer = mid
            lo = mid + 1
        else:
            hi = mid - 1
    return answer

print(my_bisect(lo, hi))
