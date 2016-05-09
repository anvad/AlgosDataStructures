# python3

class HeapBuilder:
  def __init__(self):
    self._swaps = []
    self._data = []

  def ReadData(self):
    n = int(input())
    self._data = [int(s) for s in input().split()]
    assert n == len(self._data)

  def WriteResponse(self):
    print(len(self._swaps))
    for swap in self._swaps:
      print(swap[0], swap[1])

  def GenerateSwaps(self):
    # The following naive implementation just sorts 
    # the given sequence using selection sort algorithm
    # and saves the resulting sequence of swaps.
    # This turns the given array into a heap, 
    # but in the worst case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
##    for i in range(len(self._data)):
##      for j in range(i + 1, len(self._data)):
##        if self._data[i] > self._data[j]:
##          self._swaps.append((i, j))
##          self._data[i], self._data[j] = self._data[j], self._data[i]
    self.BuildHeapMin()

  def BuildHeapMin(self):
    # for 0 based indexing
    #   LeftChild(i) = 2i+1
    #   RightChild(i) = 2i + 2
    #   Parent(i) = floor((i-1)/2)
    n = len(self._data)
    maxi = int(n/2) - 1
    for i in range(maxi, -1, -1):
      self.SiftDown(i)
    #print(self._data)

  def Parent(self, i):
    return int((i-1)/2)

  def LeftChild(self, i):
    return 2*i + 1

  def RightChild(self, i):
    return 2*i + 2

  def SiftUp(self, i):
    #while we are not already at root, and while current index is smaller than parent, swap (i.e. sift up!)
    while i > 0 and self._data[j] > self._data[i]:
      j = int((i-1)/2) #self.Parent(i)
      self._swaps.append((i, j))
      self._data[i], self._data[j] = self._data[j], self._data[i]
      i = j
      

  def SiftDown(self, i):
    #while we are not a leaf, and while current index is larger than parent, swap (i.e. sift down)
    #print("sifting down index", i, self._data[i])
    size = len(self._data)
    while i < size:
      j = i
      l = 2*i + 1 #self.LeftChild(i)
      r = 2*i + 2 #self.RightChild(i)
      if (l < size) and (self._data[l] < self._data[i]):
        j = l
      if (r < size) and (self._data[r] < self._data[j]):
        j = r
      if i != j:
        self._swaps.append((i, j))
        self._data[i], self._data[j] = self._data[j], self._data[i]
        i = j
      else:
        break
    
  def Solve(self):
    self.ReadData()
    self.GenerateSwaps()
    self.WriteResponse()

if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.Solve()
