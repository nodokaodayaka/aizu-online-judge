n, q = map(int, raw_input().split())

que = []
for _ in range(n):
  name, total = raw_input().split()
  que += [[name, total]]

total = 0
answer = []

while que:
  
  item = que.pop(0)
  name, time = item[0], int(item[1]) 

  if time > q:
    que += [[name, time - q]]
    total += q
  else:
    total += time
    answer += [[name, str(total)]]

for w in answer:
  print ' '.join(w)
