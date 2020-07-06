n = int(input())
A = list(map(int, input().split()))
q = int(input())
M = list(map(int, input().split()))

for x in M:
  dp = [[0 for _ in range(x+1)] for _ in range(n+1)]
  dp[0][0]=1
  for i in range(n):
    for j in range(x+1):
      if A[i] <= j:
        dp[i+1][j] = dp[i][j - A[i]] or dp[i][j]
      else:
        dp[i+1][j] = dp[i][j]
       
  if dp[n][x] == 1:
    print ('yes')
  else:
    print ('no')
