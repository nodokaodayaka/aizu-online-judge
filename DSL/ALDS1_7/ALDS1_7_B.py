ID, LT, RT, PARENT, SIBLING, DEGREE, TYPE, DEPTH, HEIGHT = 1,2,3,4,5,6,7,8,9

def dfs(node, i):
  l,r = i,i
  if node[LT] != -1:
    l = dfs(nodes[node[LT]], i+1)
  if node[RT] != -1:
    r = dfs(nodes[node[RT]], i+1)
  return max(l, r)

def depth(node, i):
  if node[PARENT] == -1:
    return i
  return depth(nodes[node[PARENT]], i+1)

n = int(input())
nodes = [{} for _ in range(n)]

for node in nodes:
  id, lt, rt = list(map(int, input().split()))
  nodes[id][ID] = id
  nodes[id][LT] = lt
  nodes[id][RT] = rt
  nodes[id][SIBLING] = -1
  nodes[id][TYPE] = 'root'
  nodes[id][DEPTH] = 0
  nodes[id][PARENT] = -1
  nodes[id][HEIGHT] = 0
  nodes[id][DEGREE] = 0

for node in nodes:
  id = node[ID]
  deg = 0
  if node[LT] != -1:
    nodes[node[LT]][PARENT] = id
    if node[RT] == -1:
      nodes[node[LT]][SIBLING] = -1
    else:
      nodes[node[LT]][SIBLING] = nodes[node[RT]][ID]
    deg += 1
  if node[RT] != -1:
    nodes[node[RT]][PARENT] = id
    if node[LT] == -1:
      nodes[node[RT]][SIBLING] = -1
    else:
      nodes[node[RT]][SIBLING] = nodes[node[LT]][ID]
    deg += 1
  nodes[id][DEGREE] = deg

for node in nodes:
  nodes[node[ID]][HEIGHT] = dfs(node, 0)
  nodes[node[ID]][DEPTH] = depth(node, 0)
  if nodes[node[ID]][DEGREE] == 0 and nodes[node[ID]][PARENT] != -1:
    nodes[node[ID]][TYPE] = 'leaf'
  elif nodes[node[ID]][DEGREE] != 0 and nodes[node[ID]][PARENT] != -1:
    nodes[node[ID]][TYPE] = 'internal node'

for i in range(len(nodes)):
  node = nodes[i]
  print ('node {ID}: parent = {PARENT}, sibling = {SIBLING}, degree = {DEGREE}, depth = {DEPTH}, height = {HEIGHT}, {TYPE}'
    .format(ID=node[ID], PARENT=node[PARENT], SIBLING=node[SIBLING], DEGREE=node[DEGREE], DEPTH=node[DEPTH], HEIGHT=node[HEIGHT], TYPE=node[TYPE]))
