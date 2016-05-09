# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size

class TreeOrders:
  def read(self):
    self.n = int(sys.stdin.readline())
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c

  def inOrder(self):
    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    root_ind = 0
    self.traverseTree(root_ind, "in")
    return self.result

  def traverseTree(self, cur_ind, traverseType):
    left_child_ind = self.left[cur_ind]
    right_child_ind = self.right[cur_ind]

    if traverseType == "pre":
      self.result.append(self.key[cur_ind])

    if left_child_ind != -1:
      self.traverseTree(left_child_ind, traverseType)

    if traverseType == "in":
      self.result.append(self.key[cur_ind])

    if right_child_ind != -1:
      self.traverseTree(right_child_ind, traverseType)

    if traverseType == "post":
      self.result.append(self.key[cur_ind])
      
    
  def preOrder(self):
    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    root_ind = 0
    self.traverseTree(root_ind, "pre")
    return self.result

  def postOrder(self):
    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    root_ind = 0
    self.traverseTree(root_ind, "post")
    return self.result

def main():
	tree = TreeOrders()
	tree.read()
	print(" ".join(str(x) for x in tree.inOrder()))
	print(" ".join(str(x) for x in tree.preOrder()))
	print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()
