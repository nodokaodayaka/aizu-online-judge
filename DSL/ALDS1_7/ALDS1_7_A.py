ID     = 'id'
PARENT = 'parent'
DEPTH  = 'depth'
TYPE   = 'type'
POINT  = 'POINT'

n = int(input())
nodes = [{} for _ in range(n)]
for i in range(n):
  detail = list(map(int, input().split()))
  nodes[detail[0]][ID] = detail[0]
  nodes[detail[0]][PARENT] = -1
  nodes[detail[0]][DEPTH] = 0
  nodes[detail[0]][TYPE] = 'root'
  if detail[1] > 0:
    nodes[detail[0]][POINT] = detail[2:]
  else:
    nodes[detail[0]][POINT] = []
    nodes[detail[0]][TYPE] = 'leaf'
     
for node in nodes:
  if node[POINT]:
    for i in node[POINT]:
      nodes[i][PARENT] = node[ID]

for node in nodes:
  depth = 0
  parent = node[PARENT]
  while True:
    if parent == -1:
      break
    else:
      parent = nodes[parent][PARENT]
    depth += 1
  node[DEPTH] = depth

for node in nodes:
  if node[PARENT] == -1:
    node[TYPE] = 'root'
  elif len(node[POINT])>0:
    node[TYPE] = 'internal node'

for node in nodes:
  print ('node {id}: parent = {parent}, depth = {depth}, {type}, {point}'
    .format(id=node[ID], parent=node[PARENT], depth=node[DEPTH], type=node[TYPE], point=node[POINT]))
