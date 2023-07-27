N, K = map(int, input().split())
L = [0] + list(map(int, input().split()))
dp = [[0 for _ in range(N+1)] for _ in range(3)]
dp[1][0] = 1
for idx in range(1, N+1):
    t = dp[0][idx-1] + L[idx]
    start_index = dp[1][idx-1]
    if L[idx] >= K:
        dp[0][idx] = 0
        dp[1][idx] = idx+1
        dp[2][idx] = max(t-K + dp[2][start_index-1], dp[2][idx-1])
    else:
        if t < K:
            dp[0][idx] = t
            dp[1][idx] = start_index
            dp[2][idx] = dp[2][idx-1]
        else:
            tt = t
            prev_index = start_index
            while tt >= K:
                tt -= L[start_index]
                start_index += 1
            dp[0][idx] = tt
            dp[1][idx] = start_index
            dp[2][idx] = max(dp[2][prev_index-1] + t - K, dp[2][idx-1])
print(dp[2][N])
