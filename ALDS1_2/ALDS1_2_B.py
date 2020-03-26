def selectionSort(A,N):

  count = 0
  for i in range(len(A)):
    min_pos = i
    for j in range(i, len(A)):
      if A[j] < A[min_pos]:
        min_pos = j
    if min_pos != i:
      A[i], A[min_pos] = A[min_pos], A[i]
      count += 1
  return A, count


N = int(raw_input())
A = map(int, raw_input().split())

A, count = selectionSort(A,N)
print ' '.join(map(str, A))
print count
