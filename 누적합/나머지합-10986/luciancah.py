N, M = map(int, input().split())
A = list(map(int, input().split()))


def solution(N, M, A):
    count = 0
    sum_mod = [0] * (N + 1)
    freq = [0] * M

    for i in range(N):
        sum_mod[i + 1] = (sum_mod[i] + A[i]) % M
        freq[sum_mod[i + 1]] += 1

    for m in freq:
        count += (m * (m - 1)) // 2

    count += freq[0]

    return count


answer = solution(N, M, A)
print(answer)
