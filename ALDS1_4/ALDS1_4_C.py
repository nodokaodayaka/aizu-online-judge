n = int(input())

values = {}
for _ in range(n):
  command, value = input().split()

  if command[0] == 'i':
    values[value] = value
  if command[0] == 'f':
    if value in values:
      print ('yes')
    else:
      print ('no')
