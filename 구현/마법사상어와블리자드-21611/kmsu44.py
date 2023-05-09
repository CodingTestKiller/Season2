from collections import deque
n, m = map(int, input().split())
INPUT = [[] for _ in range(n+1)]
INPUT[0] = [0 for _ in range(n+1)]
for i in range(1, n+1):
    INPUT[i] = ([0]+list(map(int, input().split())))

Blizard = []
for _ in range(m):
    Blizard.append(list(map(int, input().split())))


# 그래프 1차원화
step_size = n-1
S = deque()
i, j = 1, 1
if INPUT[i][j] != 0:
    S.insert(0, INPUT[i][j])
while True:
    # 우측 방향
    for _ in range(step_size):
        j += 1
        if INPUT[i][j] != 0:
            S.insert(0, INPUT[i][j])
    # 아래 방향
    for _ in range(step_size):
        i += 1
        if INPUT[i][j] != 0:
            S.insert(0, INPUT[i][j])
    # 왼쪽 방향
    for _ in range(step_size):
        j -= 1
        if INPUT[i][j] != 0:
            S.insert(0, INPUT[i][j])
    # 위쪽 방향
    for _ in range(step_size-1):
        i -= 1
        if INPUT[i][j] != 0:
            S.insert(0, INPUT[i][j])
    j += 1
    if i == ((n+1)//2) and j == ((n+1)//2):
        break
    else:
        if INPUT[i][j] != 0:
            S.insert(0, INPUT[i][j])
    step_size -= 2

# 블리자드 마법 범위
left = [1]
down = [3]
right = [5]
up = [7]
unit = 9

for _ in range(n // 2-1):
    left.append(left[-1] + unit)
    unit += 2
    down.append(down[-1] + unit)
    unit += 2
    right.append(right[-1] + unit)
    unit += 2
    up.append(up[-1] + unit)
    unit += 2


def arrange():
    start = 0
    end = 0
    cnt = 0
    prevdata = 0
    remove_index_list = []
    for idx, data in enumerate(S):
        if prevdata == data:
            cnt += 1
            end = idx
        else:
            if cnt >= 4:
                for i in range(start, end+1):
                    remove_index_list.append(i)
            start = idx
            prevdata = data
            cnt = 1
    if cnt >= 4:
        for i in range(start, end+1):
            remove_index_list.append(i)

    if remove_index_list:
        remove_index_list.sort(reverse=True)
        for remove_index in remove_index_list:
            if remove_index < len(S):
                Remove[S[remove_index]] += 1
                del S[remove_index]
    else:
        return False

    return True


Remove = {0: 0, 1: 0, 2: 0, 3: 0}
for d, s in Blizard:
    # 블리자드 방향 정하기
    if d == 1:
        direction = up
    elif d == 2:
        direction = down
    elif d == 3:
        direction = left
    else:
        direction = right

    # 블리자드 마법 수행
    remove_index_list = direction[:s]
    remove_index_list.sort(reverse=True)
    if remove_index_list:
        for remove_index in remove_index_list:
            if remove_index-1 < len(S):
                del S[remove_index-1]
    # 겹치는거 확인 후 삭제
    while True:
        if arrange() == False:
            break
    # 구슬 변화
    T = deque()
    cnt = 1
    if S:
        prevdata = S[0]
    else:
        continue
    T_cnt = 0
    flag = 0
    for idx, data in enumerate(S):
        if idx == 0:
            continue
        if prevdata == data:
            cnt += 1
            end = idx
        else:
            if len(T) < (n*n-1)-2:
                T.append(cnt)
                T.append(prevdata)
            else:
                break
            prevdata = data
            cnt = 1
    if len(T) < (n*n-1)-1:
        T.append(cnt)
        T.append(prevdata)

    S = T


result = 0
for i in range(1, 4):
    result += i * Remove[i]
print(result)


# 3 1
# 8 7 6
# 1 0 5
# 2 3 4
