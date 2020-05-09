quantity, num = list(map(int, input().split()))
weights = list(map(int, [input() for _ in range(quantity)]))

def truck_num(max_load, weights):
  num = 1
  tmp = 0
  for w in weights:
    if tmp + w <= max_load:
      tmp += w
    else:
      tmp = w
      num += 1
  return num
  

left = max(weights)
right = 100000 * 10000

while left < right:
  mid = (left + right) // 2
  x = truck_num(mid, weights)
  if x <= num:
    right = mid
  else:
    left = mid + 1

ans = left
print(ans)
