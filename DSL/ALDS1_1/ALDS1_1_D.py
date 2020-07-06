n = int(raw_input())
r = [int(raw_input()) for _ in range(n)]

mn = r[0]
ans = 1000000000 * (-1)

for i in range(1, len(r), 1):
  ans = max(ans, r[i] - mn)
  mn = min(mn, r[i])

print ans
