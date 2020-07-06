n = int(input())
s = list(map(int, input().split()))
q = int(input())
t = list(map(int, input().split()))

i = 0
for key in t:
  left = 0
  right = len(s)
  while left < right:
    mid = (left + right) // 2
    if key == s[mid]:
      i += 1
      break
    elif key < s[mid]:
      right = mid
    else:
      left = mid + 1
print (i)
