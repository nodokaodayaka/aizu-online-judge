s = map(str, raw_input().split())
plus = lambda x,y : x + y
minus = lambda x,y : x - y
multi = lambda x,y : x * y

stack = []

for op in s:
  if op == '+':
    y = stack.pop()
    x = stack.pop()
    stack += [plus(x,y)]
  elif op == '-':
    y = stack.pop()
    x = stack.pop()
    stack += [minus(x,y)]
  elif op == '*':
    y = stack.pop()
    x = stack.pop()
    stack += [multi(x,y)]
  else:
    stack += [int(op)]
print stack[0]



