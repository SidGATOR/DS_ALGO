from math import floor

class minHeap(object):

  def __init__(self, dary = []):
    self.ary = dary
  
  def heapify(self):
    n = len(self.ary) - 1
    for i in range(int(floor(n/2)), -1, -1):
      self.__siftDown(i)
  
  def __siftDown(self, node):
    child = node * 2 + 1

    if child > len(self.ary) - 1:
      return
    
    if child + 1 <= len(self.ary) - 1 and self.ary[child] > self.ary[child+1]:
      child += 1
    
    if self.ary[node] > self.ary[child]:
      self.ary[node], self.ary[child] = self.ary[child], self.ary[node]
      self.__siftDown(child)
    else:
      return

  def __siftUp(self, node):
    parent = int(floor((node - 1) / 2))

    if self.ary[node] < self.ary[parent]:
      self.ary[node], self.ary[parent] = self.ary[parent], self.ary[node]
    
    if parent <= 0:
      return
    else:
      self.__siftUp(parent)
  
  def pushHeap(self, value):
    self.ary += [value]
    n = len(self.ary) - 1
    self.__siftUp(n)
  
  def popHeap(self):
    n = len(self.ary) - 1
    self.ary[0], self.ary[n] = self.ary[n], self.ary[0]

    minVal = self.ary.pop()
    self.__siftDown(0)
    return minVal



  

def main():
  A = [x for x in range(5, 0,-1)]
  minH = minHeap(A)
  print(minH.ary)
  minH.heapify()
  print(minH.ary)
  minH.pushHeap(9)
  print(minH.ary)
  minH.popHeap()
  print(minH.ary)

if __name__ == "__main__":
  main()