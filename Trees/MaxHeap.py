from math import floor

class maxHeap(object):

  def __init__(self, dary = []):
    self.ary = dary
  
  def heapify(self):
    n = len(self.ary) - 1
    for i in range(int(floor(n/2)), -1, -1):
      self.__siftDown(i)
  
  def __siftDown(self, node):
    child = node * 2 + 1 # Left Child
    # Base Case where the recursion breaks
    if child > len(self.ary) - 1:
      return
    
    # check which child is greater
    if (child + 1 <= len(self.ary) - 1) and (self.ary[child] < self.ary[child +1]):
      child += 1
    
    # Swap the greater child with its parent
    if self.ary[node] < self.ary[child]:
      self.ary[node], self.ary[child] = self.ary[child], self.ary[node]
      return self.__siftDown(child)
    else:
      return

  def __siftUp(self, node):
    # Only the added node doesn't follow Heap property
    parent = int(floor((node - 1) / 2))

    if self.ary[node] > self.ary[parent]:
      self.ary[parent], self.ary[node] = self.ary[node], self.ary[parent]
    
    # Recursive break condition
    if node <= 0:
      return
    else:
      return __siftUp(parent)

  def pushHead(self, val):
    self.ary += [val]
    return self.__siftUp(len(self.ary) - 1)
  
  def popHead(self):
    n = len(self.ary) - 1
    # Swapping values at root and end of heap
    self.ary[0], self.ary[n] = self.ary[n], self.ary[0]
    maxVal = self.ary.pop()
    self.__siftDown(0)
    # return maximum value
    return maxVal

  def replaceKey(self, key, value):

    curval = self.ary[key]
    self.ary[key] = value

    if val > curval:
      self.__siftUp(key)
    
    elif curval > val:
      self.__siftDown(key)
    
    else:
      return


  

def main():
  A = [x for x in range(1,6)]
  mHeap = maxHeap(A)
  print(mHeap.ary)
  mHeap.heapify()
  print(mHeap.ary)
  print(mHeap.popHead(), mHeap.ary)


if __name__ == "__main__":
  main()
