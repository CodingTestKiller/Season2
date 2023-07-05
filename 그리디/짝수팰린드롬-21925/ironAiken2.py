from sys import stdin
input = stdin.readline

n = int(input())
arr = [int(x) for x in input().split()]
stack = []
cnt = 0
s, e = 0, 0
is_even = 0

for i, data in enumerate(arr):
    if not stack or stack[-1] != data:
        if not stack:
            s = i
            is_even = 0
        stack.append(data)
        is_even += 1
        continue

    if stack[-1] == data:
        stack.pop()
        e = i
        is_even += 1
        if not stack:
            cnt += 1
            if is_even % 2 != 0:
                print(-1)
                exit()


def is_validate(s: int, e: int) -> None:
    if len(arr[s:e+1]) % 2 != 0:
        print(-1)
        exit()
    while s < e:
        if arr[s] != arr[e]:
            print(-1)
            exit()
        s += 1
        e -= 1


is_validate(s, e)
print(cnt)
