import ctypes

class DynamicArray(object):

    ##Making a constructor to initialize the values of a new array

    def __init__(self):
        #Index
        self.n = 0
        #Capacity
        self.capacity = 1
        #Making an array
        self.A = self.make_array(self.capacity)


    ## Get the length of the array

    def __len__(self):
        return self.n

    ## Get the element at index K

    def __getitem__(self,K):
        ## Checking for K
        if not 0 <= K <= self.n:
            return IndexError('K out of bounds!')

        return self.A[K]

    ## Append

    def append(self,element):

        # Check if array has capacity
        if self.n == self.capacity:
            self._resize(2*self.capacity) # 2x

        self.A[self.n] = element
        self.n += 1

    ## Resizing of the array

    def _resize(self,new_capacity):

        ## Allocating a larger array
        B = self.make_array(new_capacity)

        ## Setting the current values of A to B
        for i in range(self.n):
            B[i] = self.A[i]

        ## Assigning 'A' to the new array

        self.A = B
        self.capacity = new_capacity

    ## Making new array
    def make_array(self,new_capacity):
        ## Using ctypes lib to allocate memory
        return (new_capacity * ctypes.py_object)()

