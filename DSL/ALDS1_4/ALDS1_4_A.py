n = int(input())
s = input().split()
q = int(input())
t = input().split()

i = 0
for tt in t:
  if tt in s:
    i += 1

print (i)
