def BubbleSort(C,N):
  for _ in C:
    for i in range(len(C)-1, 0, -1):    
      if C[i][-1:] < C[i-1][-1:]:
        C[i], C[i-1] = C[i-1], C[i]
  return C

def SelectionSort(C,N):
  for i in range(len(C)):
    min_pos = i
    for j in range(i+1, len(C)):
      if int(C[j][-1]) < int(C[min_pos][-1]):
        min_pos = j
    C[i], C[min_pos] = C[min_pos], C[i]
  return C

N = int(raw_input())
card = map(str, raw_input().split())

card0 = card
card1 = card[:]
card0 = BubbleSort(card0,N)
card1 = SelectionSort(card1,N)

print ' '.join(card0)
print "Stable"
print ' '.join(card1)
if card0 == card1:
  print "Stable"
else:
  print "Not stable"
