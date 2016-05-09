# python3

#import sys
import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size

class Rope:
  def __init__(self, s):
    self.s = s
    lens = len(s)
    for i in range(lens):
      #print(i, s[i], sep=":", end=" ")
      insert(i)
    #print("")
    #print(self.result())
  def result(self):
    global root
    self.res = []
    #return self.s
    #traverse tree in order
    self.traverseTree(root, "in")
    return ''.join(self.res)
  def printTree(self, cur_node, label):
    self.res = []
    self.traverseTree(cur_node, "in")
    post = ""
    if cur_node != None:
      #post = str(findIndex(cur_node)) + ":" + self.s[cur_node.key] + ":" + str(cur_node.key)
      post = self.s[cur_node.key] + ":" + str(cur_node.key)
    print(label, ''.join(self.res), post)
  def traverseTree(self, cur_node, traverseType):
    if cur_node == None:
      return
    leftChild = cur_node.left
    rightChild = cur_node.right
    if traverseType == "pre":
      self.res.append(self.s[cur_node.key])
    if leftChild != None:
      self.traverseTree(leftChild, traverseType)
    if traverseType == "in":
      self.res.append(self.s[cur_node.key])
    if rightChild != None:
      self.traverseTree(rightChild, traverseType)
    if traverseType == "post":
      self.res.append(self.s[cur_node.key])
  def process(self, i, j, k):
    # Write your code here
    global root
    self.splice(i, j, k)

  def splice(self, fr, to, bf):
    global root
    #print("frm to before", fr, to, bf)
    #self.printTree(root, "root: ")
    #(foundNode, root) = find(root, fr)
    (middle, right) = split(root, to + 1)
    #self.printTree(middle, "middle+left : ")
    #self.printTree(right,  "right       : ")
    (left, middle) = split(middle, fr)
    #self.printTree(left,   "left        : ")
    #self.printTree(middle, "middle      : ")
    #left is left of fr, middle is s[fr..to], right is s[to+1..]
    left = merge(left, right) #merge the left and right pieces
    #self.printTree(left,   "left+right  : ")
    (left, right) = split(left, bf) #split the recomined tree again, so we can insert the middle
    #self.printTree(left,   "new left    : ")
    middle = merge(left, middle)
    #self.printTree(middle,   "new middle  : ")
    root = merge(middle, right)
    #self.printTree(root,   "new root    : ")
    return root


#we can use a splay tree to store the string and to cut and merge the pieces
#what'll be the key? index position or the char?
#the char itself won't change when we re-arrange, so key must be current index position
#then we can use find() to find and split left, middle, right portions of string
#but after we split, the current index gets shifted left for the middle and right trees by the same constant for each tree
#so, perhaps we can just store/update this constant as a property of the root node only
#and when finding a key, we'll just subtract this constant from x, to map it to the index stored.

#N.size = N.left.size + N.right.size + 1
#well, when we use order statistics, we don't really care what the key is..
#so we can literally replace the key comparison (used in find)
#we'll change the update function to recompute size and not use key
#we'll change the find function to use the size attribute rather than the key attribute
#insert and erase also look at key
#so, scratch that, we won't change the find function, we'll just use a new orderStatistic function where we were using find.
#and let key be defined once (at the time of insertion) to be the original index of the character
#later, for printing, we'll use this index to retrieve the actual char from orig array
#but then, find will get screwed up after the first split and merge, since left subtree could have keys larger than right sub-tree!


# Splay tree implementation

# Vertex of a splay tree
class Vertex:
  def __init__(self, key, size, left, right, parent):
    (self.key, self.size, self.left, self.right, self.parent) = (key, size, left, right, parent)

def update(v):
  if v == None:
    return
  v.size = 1 + (v.left.size if v.left != None else 0) + (v.right.size if v.right != None else 0)
  if v.left != None:
    v.left.parent = v
  if v.right != None:
    v.right.parent = v

def smallRotation(v):
  parent = v.parent
  if parent == None:
    return
  grandparent = v.parent.parent
  if parent.left == v:
    m = v.right
    v.right = parent
    parent.left = m
  else:
    m = v.left
    v.left = parent
    parent.right = m
  update(parent)
  update(v)
  v.parent = grandparent
  if grandparent != None:
    if grandparent.left == parent:
      grandparent.left = v
    else: 
      grandparent.right = v

def bigRotation(v):
  if v.parent.left == v and v.parent.parent.left == v.parent:
    # Zig-zig
    smallRotation(v.parent)
    smallRotation(v)
  elif v.parent.right == v and v.parent.parent.right == v.parent:
    # Zig-zig
    smallRotation(v.parent)
    smallRotation(v)    
  else: 
    # Zig-zag
    smallRotation(v);
    smallRotation(v);

# Makes splay of the given vertex and makes
# it the new root.
def splay(v):
  if v == None:
    return None
  while v.parent != None:
    if v.parent.parent == None:
      smallRotation(v)
      break
    bigRotation(v)
  return v

# Searches for the given key in the tree with the given root
# and calls splay for the deepest visited node after that.
# Returns pair of the result and the new root.
# If found, result is a pointer to the node with the given key.
# Otherwise, result is a pointer to the node with the smallest
# bigger key (next value in the order).
# If the key is bigger than all keys in the tree,
# then result is None.
def findk(root, key): 
  v = root
  last = root
  nextv = None
  while v != None:
    if v.key >= key and (nextv == None or v.key < nextv.key):
      nextv = v    
    last = v
    if v.key == key:
      break    
    if v.key < key:
      v = v.right
    else: 
      v = v.left      
  root = splay(last)
  return (nextv, root)

def find(root, index):
  #global rope
  foundNode = findi(root, index)
  newRoot = root
  if foundNode != None:
    newRoot = splay(foundNode)
  return (foundNode, newRoot)

def findIndex_old(cur_node):
  if cur_node == None:
    return -1
  if cur_node.left != None:
    return cur_node.left.size
  else:
    return 0

#finds the node whose index position matches the zero based index passed in
def findi_test(root, index):
  #print("findi index to find, root's index", index, str(findIndex(root)))
  if root.size <= index:
    #then we need to find largest node, splay it up and return it
    pass
  v = root
  last = root
  nextv = None
  cur_index = 0
  while v != None:
    cur_index = cur_index + (v.left.size if v.left != None else 0)
    if v.key >= key and (nextv == None or v.key < nextv.key):
      nextv = v    
    last = v
    if v.key == key:
      break    
    if v.key < key:
      v = v.right
    else: 
      v = v.left      
  root = splay(last)
  return (nextv, root)

def findi(root, index):
  global rope
  #print("findi index to find", index)
  if root == None:
    return root
  #if rope != None:
    #post = rope.s[root.key] + ":" + str(root.key)
    #print("root is", post)
  cur_index = 0
  if root.left != None:
    cur_index = root.left.size
  if index == (cur_index):
    return root
  elif index < (cur_index):
    #print("going to left child")
    return findi(root.left, index)
  elif index > (cur_index):
    #print("going to right child")
    return findi(root.right, index - cur_index - 1)

#splits tree into left and right
#right tree root = key, if key was found in tree, else next bigger key becomes root of right tree
#root of left tree, is the left child of key (or nextv) after the key is splayed
#here, key is really the index at which to split
def split(root, key):  
  (result, root) = find(root, key)
  if result == None:
    #print("did not find index", key)
    return (root, None)
  #print("found index", key, ". result is ", str(findIndex(result)), str(result.key))
  right = splay(result)
  left = right.left
  #now here, my left's root has correct index, but if left's root has right side children
  right.left = None
  if left != None:
    left.parent = None
  update(left)
  update(right)
  return (left, right)


#this assumes left and right tree don't overlap
#find the left-most node in right tree
#splay it, so it becomes root
#obviously this node will not have a left child
#so, simply attach the left tree as a child of the right tree
def merge(left, right):
  if left == None:
    return right
  if right == None:
    return left
  while right.left != None:
    right = right.left
  right = splay(right)
  right.left = left
  update(right)
  return right

# Code that uses splay tree to solve the problem
                                    
#root = None

def insert(x):
  global root
  (left, right) = split(root, x)
  new_vertex = None
  if right == None or right.key != x:
    new_vertex = Vertex(x, x+1, None, None, None)  
  root = merge(merge(left, new_vertex), right)

def erase(x):
  global root
  (left, right) = split(root, x)
  if right != None and right.key == x:
    if right.left != None:
      right.left.parent = None
    if right.right != None:
      right.right.parent = None
    root = merge(left, merge(right.left, right.right))
  else:
    #x not found, so just recombine
    root = merge(left, right)

def search(x): 
  global root
  # Implement find yourself
  (v,root) = find(root, x)
  if (v != None) and (v.key == x):
    return True
  return False
  


rope = None
root = None
rope = Rope(sys.stdin.readline().strip())
q = int(sys.stdin.readline())
for _ in range(q):
  i, j, k = map(int, sys.stdin.readline().strip().split())
  rope.process(i, j, k)
print(rope.result())
#rope.PrintResult()
