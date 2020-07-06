N, W = map(int, input().split())
v = [0] * N
w = [0] * N
dp = [0] * (W+1)
for i in range(N):
    v[i],w[i] = list(map(int, input().split()))

for i in range(N):
    for j in range(W, w[i]-1, -1):
        #print(dp, v[i], i, j)
        dp[j] = max(dp[j], dp[j-w[i]] + v[i])
#print(dp)
print(dp[W])
