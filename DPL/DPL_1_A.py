n, m = map(int, input().split())
c = list(map(int, input().split()))
INF = float('inf')
dp =[0] + [INF for _ in range(n)]

#print(c)

for i in range(m):
    for j in range(n+1):
        if j - c[i] >= 0:
            dp[j] = min(dp[j], dp[j-c[i]] + 1)
        pass
    #print(dp, c[i])
print(dp[n])
