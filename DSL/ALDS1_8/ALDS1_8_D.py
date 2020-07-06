class Node:
    def __init__(self, key, priority, parent=None, left=None, right=None):
        self.key = key
        self.priority = priority
        self.parent = parent
        self.left = left
        self.right = right

class BinaryTree:
    root = None

    def add(self, node, key, priority):
        if self.root is None:
            self.root = Node(key, priority)
            return self.root

        current = None
        node = self.root
        while node is not None:
            current = node
            if key < node.key:
                node = node.left
            else:
                node = node.right
        new_node = Node(key, priority, current)

        if new_node.key < current.key:
            current.left = new_node
        elif current.key < new_node.key:
            current.right = new_node
        #print(new_node, new_node.key, new_node.priority, new_node.parent, new_node.left, new_node.right)
        #print(current, current.key, current.priority, current.parent, current.left, current.right)
        return new_node

    def preOrder(self, node=None):
        if node is None:
            return
        print(' ' + node.key, end='')
        self.preOrder(node.left) 
        self.preOrder(node.right) 

    def inOrder(self, node=None):
        if node is None:
            return
        self.preOrder(node.left) 
        print(' ' + node.key, end='')
        self.preOrder(node.right) 

    def postOrder(self, node=None):
        if node is None:
            return
        self.preOrder(node.left) 
        self.preOrder(node.right) 
        print(' ' + node.key, end='')

n = int(input())
command_list = [list(input().split()) for _ in range(n)]

bTree = BinaryTree()
for command in command_list:
    if command[0] == 'insert':
        _, key, priority = command
        node = bTree.add(None, key, priority)
        pass
    if command[0] == 'print':
        bTree.preOrder(bTree.root)
        print()
        bTree.inOrder(bTree.root)
        print()
        bTree.postOrder(bTree.root)
        print()
        pass
    if command[0] == 'find':
        pass
    if command[0] == 'delete':
        pass




