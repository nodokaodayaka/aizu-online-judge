class LinkedList:

  def __init__(self, id = None):
    self.id = id
    self.next = self
    self.prev = self

  def insert(self, id):
    new = LinkedList(id)
    new.next = self.next
    new.prev = self
    self.next = new
    self.next.prev = new

  def delete(self, id):
    cur = self.next
    while cur.id is not None:
      if cur.id == id:
        cur.next.prev = cur.prev
        cur.prev.next = cur.next
        break
      cur = cur.next
    pass

  def printList(self):
    node = self.next
    while node.id is not None:
      print node, node.__dict__
      node = node.next


n = int(raw_input())

linkedList = LinkedList()
for _ in range(n):
  var = raw_input().split()
  command = var[0]
  if command == 'insert':
    linkedList.insert(var[1])
    pass
  if command == 'delete':
    linkedList.delete(var[1])
    pass
  if command == 'deleteFirst':
    #linkedList.deleteFirst()
    pass
  if command == 'deleteLast':
    #linkedList.deleteLast()
    pass
linkedList.printList()
