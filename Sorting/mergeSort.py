from math import ceil

class mergeSort(object):
  def __init__(self):
    pass
  
  def sort(self, dary, l, r):
    # left array is L[l:m] inclusive
    # right array is R[m:r] inclusive
   
    if l < r:
      m = int(l + (r-l)/2)
      self.sort(dary, l, m)

      self.sort(dary, m + 1, r)

      self.__merge(dary, l, m, r)
    

  def __merge(self, dary, l, m, r):
    # Find the sizes of left array and right array
    n1 = m - l + 1
    n2 = r - m 
    # Make a copy of the Arrays into tmp array
    L = [dary[x] for x in range(l, m+1)]
    R = [dary[x] for x in range(m+1,r+1)]

    i,j,k = 0, 0, l
    while(i < n1 and j < n2):
      if L[i] < R[j]:
        dary[k] = L[i]
        i += 1
        k += 1
      else:
        dary[k] = R[j]
        j += 1
        k += 1
    
    while(i < n1):
      dary[k] = L[i]
      i += 1
      k += 1
    
    while(j < n2):
      dary[k] = R[j]
      j += 1
      k += 1

def main():
  A = [5,4,7,2, 2, -22, -1, 46,78,21]
  mergeSorted = mergeSort()
  mergeSorted.sort(A, 0, len(A) - 1)
  print(A)

if __name__ == '__main__':
  main()

