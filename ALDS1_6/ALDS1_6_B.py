def partition(A, p, r):
  x = A[r]
  i = p -1

  for j in range(p, len(A)):
    if A[j] <= x:
      i += 1
      A[i], A[j] = A[j], A[i]
  return i

n = int(input())
A = list(map(int, input().split()))
cnt = partition(A, 0, len(A)-1)

ans = []
for i, j in enumerate(A):
  if i == cnt:
    ans.append("["+str(j)+"]")
  else:
    ans.append(str(j))

print (" ".join(ans))
