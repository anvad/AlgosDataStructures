# python3

class HeapBuilderMin:
  def __init__(self):
    self._swaps = []
    self._data = []

  def ReadData(self):
    n = int(input())
    self._data = [int(s) for s in input().split()]
    assert n == len(self._data)

  def ReadData2(self, data):
    n = len(data)
    self._data = data
    #assert n == len(self._data)
    
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
      #self._swaps.append((i, j))
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
        #self._swaps.append((i, j))
        self._data[i], self._data[j] = self._data[j], self._data[i]
        i = j
      else:
        break

  def ExtractMin(self):
    size = len(self._data)
    if (size == 0):
      print("Nothing to extract. no more elements left in queue!")
    else:
      result = self._data[0]
      self._data[0] = self._data[size-1]
      self._data.pop()
      if (size > 1):
        self.SiftDown(0)
    return result

  def GetMin(self):
    size = len(self._data)
    if (size == 0):
      print("Nothing to GetMin. no more elements left in queue!")
    else:
        return self._data[0]

  def ChangePriority(self, i, p):
      oldp = self._data[i]
      self._data[i] = p
      if p > oldp:
          self.SiftDown(i)
      else:
          self.SiftUp(i)
    
  def Solve(self):
    self.ReadData()
    self.GenerateSwaps()
    self.WriteResponse()

class JobQueue:
    def read_data(self):
        self.num_workers, m = map(int, input().split())
        self.jobs = list(map(int, input().split()))
        assert m == len(self.jobs)

    def write_response(self):
        for i in range(len(self.jobs)):
          print(self.assigned_workers[i], self.start_times[i]) 

    def assign_jobs_orig(self):
        # TODO: replace this code with a faster algorithm.
        self.assigned_workers = [None] * len(self.jobs)
        self.start_times = [None] * len(self.jobs)
        next_free_time = [0] * self.num_workers
        for i in range(len(self.jobs)):
          next_worker = 0
          for j in range(self.num_workers):
            if next_free_time[j] < next_free_time[next_worker]:
              next_worker = j
          self.assigned_workers[i] = next_worker
          self.start_times[i] = next_free_time[next_worker]
          next_free_time[next_worker] += self.jobs[i]

    def assign_jobs(self):
        # TODO: replace this code with a faster algorithm.
        self.assigned_workers = [None] * len(self.jobs)
        self.start_times = [None] * len(self.jobs)
        next_free_time = [0] * self.num_workers
        #create min-heap with "2 element tuples" as each element of the heap
        #element 1 of the tuple is the next_free_time of a given thread.
        #   This will act like a reverse-priority: i.e. the smaller this number, the higher its priority
        #element 2 of the tuple is the index of that thread
        #so, GetMin() will always find the thread with smallest next_free_time.
        #   If two or more threads have same next_free_time, then thread with smallest index will get selected
        #and, each time we assign a thread to a job, we'll increase that thread's "reverse-priority" by that job's running time and SiftDown()
        heapTh = HeapBuilderMin()
        heapTh.ReadData2([(0,i) for i in range(self.num_workers)]) #this is already a min-heap, as elements are sorted in ascending order
        
        for i in range(len(self.jobs)):
          next_free_time2,next_worker = heapTh.GetMin()
          self.assigned_workers[i] = next_worker
          self.start_times[i] = next_free_time[next_worker]
          next_free_time[next_worker] += self.jobs[i]
          heapTh.ChangePriority(0, (next_free_time[next_worker],next_worker))

    def solve(self):
        self.read_data()
        self.assign_jobs()
        self.write_response()

if __name__ == '__main__':
    job_queue = JobQueue()
    job_queue.solve()

