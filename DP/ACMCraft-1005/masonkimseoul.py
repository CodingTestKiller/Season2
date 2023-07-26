from collections import deque
import sys

T = int(sys.stdin.readline())
for _ in range(T):
    num_buildings, num_order = map(int, input().split())
    t_build = [0] + list(map(int, input().split()))
    matrix = [[] for _ in range(num_buildings + 1)]
    num_parents = [0] * (num_buildings + 1)

    for _ in range(num_order):
        a, b = map(int, input().split())
        matrix[a].append(b)
        num_parents[b] += 1

    obj = int(input())
    q = deque([])

    for i in range(1, len(num_parents)):
        if num_parents[i] == 0:
            q.append(i)
            num_parents[i] = -1

    init_level = 0
    time_consumed = [0] * (len(num_parents) + 1)

    for q_value in q:
        time_consumed[q_value] = t_build[q_value]

    while q:

        building = q.popleft()

        if building == obj:
            break

        next_buildings = matrix[building]

        for next_building in next_buildings:
            time_consumed[next_building] = max(time_consumed[next_building], time_consumed[building] + t_build[next_building])
            num_parents[next_building] -= 1

        for i in range(1, len(num_parents)):
            if num_parents[i] == 0:
                q.append(i)
                num_parents[i] = -1

    print(time_consumed[obj])