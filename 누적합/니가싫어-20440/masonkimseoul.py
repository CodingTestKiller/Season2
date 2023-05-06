import sys

N = int(sys.stdin.readline())
T_dict = {}
for _ in range(N):
    T_in, T_out = map(int, sys.stdin.readline().split())
    T_dict[T_in] = T_dict.get(T_in, 0) + 1
    T_dict[T_out] = T_dict.get(T_out, 0) - 1

count = -1
T_max = [None, None]
mosquitoes = sorted(T_dict.keys())
result = 0
flag = False

for i in mosquitoes:
    result += T_dict[i]
    if result > count:
        count = result
        T_max[0] = i
        flag = True
    elif result < count and flag:
        T_max[1] = i
        flag = False

print(count)
print(T_max[0], T_max[1])