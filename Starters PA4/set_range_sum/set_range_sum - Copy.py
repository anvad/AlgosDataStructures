# python3

from sys import stdin

# Splay tree implementation

# Vertex of a splay tree
class Vertex:
  def __init__(self, key, sum, left, right, parent):
    (self.key, self.sum, self.left, self.right, self.parent) = (key, sum, left, right, parent)

def update(v):
  if v == None:
    return
  v.sum = v.key + (v.left.sum if v.left != None else 0) + (v.right.sum if v.right != None else 0)
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
def find(root, key): 
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

#splits tree into left and right
#right tree root = key, if key was found in tree, else next bigger key becomes root of right tree
#root of left tree, is the left child of key (or nextv) after the key is splayed
def split(root, key):  
  (result, root) = find(root, key)  
  if result == None:    
    return (root, None)
  right = splay(result)
  left = right.left
  right.left = None
  if left != None:
    left.parent = None
  update(left)
  update(right)
  return (left, right)


#this assumes left and right tree don't overlap
#find the smallest key in right tree
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

def nextx(v):
  if v.right != None:
    return leftDescendant(v.right)
  else:
    rightAncestor(v)

def leftDescendant(v):
  if v.left != None:
    return leftDescendant(v.left)
  return v

def rightAncestor2(v):
  parent = v.parent
  if (parent.right!= None) and (parent.right == v):
    return rightAncestor(parent)
  return parent

def rightAncestor(v):
  if v.key < v.parent.key:
    return v.parent
  else:
    rightAncestor(x.parent)

# Code that uses splay tree to solve the problem
                                    
root = None

def insert(x):
  global root
  (left, right) = split(root, x)
  new_vertex = None
  if right == None or right.key != x:
    new_vertex = Vertex(x, x, None, None, None)  
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

def erase2(x):
  global root
  v,root = find(root, x)
  if (v != None) and (v.key == x):
    #v exists and v is the root, so delete v
    v = splay(v)
    if v.left != None:
      left = v.left
      while left.right != None:
        left = left.right
      left.right = v.right
      left.parent = None
      update(left.right)
      update(left.left)
      update(left)
      root = left
    else:
      #the node to be erased doesn't have a left child.
      #so, after we erase it, the right child becomes the new root
      if v.right != None:
        root = v.right
        v.right.parent = None
        update(root)
      else:
        #there is no right child either.. so after we erase this.. we have no more tree!
        root = None
  else:
    #x is not in the tree, so ignore!
    pass

def erase_old(x): 
  global root
  # Implement erase yourself
  v,root = find(root, x)
  if (v != None) and (v.key == x):
    #v exists and v is the root, so delete v
    if v.left != None:
      leftLargest,root = find(v.left, float("inf"))
      #root = splay(leftLargest)
      root.right = v.right
      update(root)
    else:
      #the node to be erased doesn't have a left child.
      #so, after we erase it, the right child becomes the new root
      if v.right != None:
        root = v.right
        v.right.parent = None
      else:
        #there is no right child either.. so after we erase this.. we have no more tree!
        root = None
  else:
    #x is not in the tree, so ignore!
    pass
  pass

def search(x): 
  global root
  # Implement find yourself
  (v,root) = find(root, x)
  if (v != None) and (v.key == x):
    return True
  return False
  
def sum(fr, to):
  global root
  (left, middle) = split(root, fr)
  (middle, right) = split(middle, to + 1)
  ans = 0
  # Complete the implementation of sum
  if middle != None:
    ans = middle.sum
  middle = merge(left, middle)
  root = merge(middle, right)
  return ans

MODULO = 1000000001
n = int(stdin.readline())
last_sum_result = 0
for i in range(n):
  line = stdin.readline().split()
  if line[0] == '+':
    x = int(line[1])
    insert((x + last_sum_result) % MODULO)
  elif line[0] == '-':
    x = int(line[1])
    erase((x + last_sum_result) % MODULO)
  elif line[0] == '?':
    x = int(line[1])
    print('Found' if search((x + last_sum_result) % MODULO) else 'Not found')
  elif line[0] == 's':
    l = int(line[1])
    r = int(line[2])
    res = sum((l + last_sum_result) % MODULO, (r + last_sum_result) % MODULO)
    print(res)
    last_sum_result = res % MODULO
