def insertionSort(A, n, g):
  cnt = 0
  for i in range(g,n):
    v = A[i]
    j = i-g
    while j >= 0 and A[j] > v:
      A[j+g] = A[j]
      j -= g
      cnt += 1
    A[j+g] = v
  return cnt

def shellSort(A, n):
  h = 1
  g = []
  g.append(h)
  while 3*h+1 < N:
    h = 3*h+1
    g.append(h)
  
  g.reverse()
  print len(g)
  print ' '.join(map(str, g))
  cnt = 0
  for G in g:
    cnt += insertionSort(A, N, G)
  print cnt
  print '\n'.join(map(str, A))

N = int(raw_input())
A = []
for _ in range(N):
  A += [int(raw_input())]
shellSort(A,N)

