def bubble(N, A):
  count = 0
  flag = True
  while flag:
    flag = False
    for i in range(N-1, 0, -1):
      if A[i-1] > A[i]:
        count += 1
        A[i], A[i-1] = A[i-1], A[i]
        flag = True

  return count, A

n = int(raw_input())
a = map(int, raw_input().split())
count, a = bubble(n,a)

print ' '.join(map(str, a))
print count
