class Node(object):
  def __init__(self, k, v, left=None, right=None, parent=None):
    self.key = k
    self.value = v
    self.left = left
    self.right = right
    self.parent = parent
    self.balance = 0
    self.height = 0

  def hasLeftChild(self):
    return bool(self.left)
  
  def hasRightChild(self):
    return bool(self.right)
  
  def hasBothChild(self):
    return self.hasLeftChild() and self.hasRightChild()

class binaryTree(Node):
  def __init__(self):
    self.root = None
    self.stackUp = []
  
  def _put(self, k, v, curNode):
    if curNode:
      self.stackUp += [curNode]
      if k < curNode.key:
        if curNode.left is None:

          curNode.left = Node(k,v, parent = curNode)
        else:
          self._put(k, v, curNode.left)
      elif k > curNode.key:
        if curNode.right is None:
          curNode.right = Node(k, v, parent = curNode)
        else:
          self._put(k, v, curNode.right)
  
  def put(self, k, v):
    if self.root is None:
      self.root = Node(k,v)
    else:
      self._put(k, v, self.root)
      
      

  
  def __setitem__(self, k, v):
    self.put(k,v)

  def preOrder(self, Node):
    print(Node.key, Node.value, Node.height, Node.balance)
    if Node.left:
      self.preOrder(Node.left)
    if Node.right:
      self.preOrder(Node.right)
  
  def initBalanceFactor(self, Node):
    if Node.left:
      self.initBalanceFactor(Node.left)
    if Node.right:
      self.initBalanceFactor(Node.right)
    
    if Node.hasBothChild():
      Node.balance = Node.left.height - Node.right.height
      Node.height = max(Node.left.height, Node.right.height) + 1
    else:
      Node.height = 0
      if Node.hasLeftChild():
        Node.balance = Node.left.height + 1
        Node.height += 1
      elif Node.hasRightChild():
        Node.balance = -1 - Node.right.height 
        Node.height += 1
      elif not Node.hasBothChild():
        Node.balance = 0

  def redoBalance(self):
      while(len(self.stackUp)):
        Node = self.stackUp.pop()
        if Node.hasBothChild():
          Node.balance = Node.left.height - Node.right.height
          Node.height = max(Node.left.height, Node.right.height) + 1
        else:
          if Node.hasLeftChild():
            Node.balance = Node.left.height + 1
            Node.height += 1
          elif Node.hasRightChild():
            Node.balance = -1 - Node.right.height 
            Node.height += 1
          elif not Node.hasBothChild():
            Node.balance = 0
        
        if Node.balance == 0:
          self.stackUp = []
  
  def initStackClean(self):
    self.stackUp = []
      

    
      

def main():
  A = [(10, "today"), (7, "you"), (40, "thanks"), (3, "how") ,(1, "hello"), (5, "are"), (8, "doing"), (30, "for"), (20, "asking"), (35, "am"), (25, "I"), (45, "doing"), (60, "fine")]
  bt = binaryTree()
  for k,v in A:
    bt[k] = v
  bt.initBalanceFactor(bt.root)
  bt.initStackClean()
  bt[9] = "test"
  bt.redoBalance()
  bt[29] = "test2"
  bt.redoBalance()
  bt.preOrder(bt.root)

if __name__ == "__main__":
  main()
