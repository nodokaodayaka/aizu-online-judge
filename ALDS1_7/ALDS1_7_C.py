ID,LEFT,RIGHT = 0,1,2
n = int(input())

preorder_list = []
def preorder(node):
  preorder_list.append(node[ID])
  if node[LEFT] != -1:
    preorder(nodes[node[LEFT]])
  if node[RIGHT] != -1:
    preorder(nodes[node[RIGHT]])

inorder_list = []
def inorder(node):
  if node[LEFT] != -1:
    inorder(nodes[node[LEFT]])
  inorder_list.append(node[ID])
  if node[RIGHT] != -1:
    inorder(nodes[node[RIGHT]])

postorder_list = []
def postorder(node):
  if node[LEFT] != -1:
    postorder(nodes[node[LEFT]])
  if node[RIGHT] != -1:
    postorder(nodes[node[RIGHT]])
  postorder_list.append(node[ID])

nodes = []
for _ in range(n):
  id, left, right = list(map(int, input().split()))
  nodes.append({ID:id, LEFT:left, RIGHT:right})

root = {}
for node in nodes:
  if node[ID] == 0:
    root = node
    break

preorder(root)
inorder(root)
postorder(root)
print ('Preorder')
print (' '.join(map(str, preorder_list)))
print ('Inorder')
print (' '.join(map(str, inorder_list)))
print ('Postorder')
print (' '.join(map(str, postorder_list)))
