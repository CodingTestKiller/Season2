from sys import stdin
input = stdin.readline

n, m = [int(x) for x in input().split()]
arr = [[0 for _ in range(n+1)]] + [[0] + [int(x) for x in input().split()] for _ in range(n)]

for a in arr:
    print(a)

x, y = (n+1)//2, (n+1)//2
ans = 0

# 좌 하 우 상 순서
moves = [[],[0,-1],[1,0],[0,1],[-1,0]]

# 구슬 파괴 후 구슬 이동
def distroy():
    global ans

    d, s = [int(x) for x in input().split()]
    next_x, next_y = x, y

    # 구슬 부셔버리기
    if d == 1:
        xx, yy = -1, 0
    elif d == 2:
        xx, yy = 1, 0
    elif d == 3:
        xx, yy = 0, -1
    elif d == 4:
        xx, yy = 0, 1

    for _ in range(s):
        next_x += xx
        next_y += yy

        # ans += arr[next_x][next_y]
        arr[next_x][next_y] = 0

def get_all_marbles() -> list:
    flag = 0
    dist = 1
    dirc = 1
    next_x, next_y = x, y

    marbles = []
    marbles.append(arr[next_x][next_y])

    while True:
        if next_x == 1 and next_y == 1:
            return marbles
        
        for _ in range(dist):
            if next_x == 1 and next_y == 1:
                return marbles
            next_x += moves[dirc][0]
            next_y += moves[dirc][1]
            if arr[next_x][next_y] != 0:
                marbles.append(arr[next_x][next_y])

        dirc += 1 if dirc < 4 else -3

        flag += 1
        if flag >= 2:
            dist += 1
            flag = 0

def explore_marbles():
    global current, ans

    flag = True
    save = 0

    while flag:
        flag = False
        cnt = 0
        
        for i, num in enumerate(current):
            if num == save:
                cnt += 1
            else:            
                if cnt >= 4:
                    ans += save * cnt
                    for ii in range(1, cnt + 1):
                        current[i-ii] = -1
                        flag = True

                save = num
                cnt = 1
        
        result = []


        for num in current:
            if num != -1:
                result.append(num)
        current = result

def change_marbles():
    global current

    cnt = 0
    save = 0
    result = []

    for num in current[1:]:
        if num == save:
            cnt += 1
        else:
            result.append(cnt)
            result.append(save)
            save = num
            cnt = 1
    current = result[1:]

def fill_the_marbles():
    flag = 0
    dist = 1
    dirc = 1
    i = 1
    next_x, next_y = x, y
    arr[next_x][next_y] = 0

    while True:
        if next_x == 1 and next_y == 1:
            return
        
        for _ in range(dist):
            if next_x == 1 and next_y == 1:
                return
            next_x += moves[dirc][0]
            next_y += moves[dirc][1]

            try:
                arr[next_x][next_y] = current[i]
            except IndexError:
                arr[next_x][next_y] = 0
            i += 1

        dirc += 1 if dirc < 4 else -3

        flag += 1
        if flag >= 2:
            dist += 1
            flag = 0

for _ in range(m):

    distroy()
    get_all_marbles()
    current = get_all_marbles()
    explore_marbles()
    change_marbles()
    fill_the_marbles()


print(ans)