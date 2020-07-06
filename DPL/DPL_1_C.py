N, W = map(int, input().split())
v = [0] * N
w = [0] * N

for i in range(N):
    v[i], w[i] = list(map(int, input().split()))

dp = [[0 for _ in range(W+1)] for _ in range(N+1)]
dp = [0 for _ in range(W+1)]

for i in range(N):
    for j in range(W+1):
        if j >= w[i]:
            dp[j] = max(dp[j], dp[j-w[i]] + v[i])
            #print(dp)
            pass

print(dp[W])
