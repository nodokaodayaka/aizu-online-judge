from collections import deque

d = deque()
n = int(input())
items = [map(str, input().split()) for _ in range(n)]

for item in items:
  line = list(item)

  if line[0] == 'insert':
    d.append(line[1])
  elif line[0] == 'delete':
    if line[1] in d:
      d.remove(line[1])
  elif line[0] == 'deleteFirst':
    d.popleft()
  elif line[0] == 'deleteLast':
    d.pop()

ans = []
print (d)
while d:
  ans.append(d.pop())

print (' '.join(ans))
