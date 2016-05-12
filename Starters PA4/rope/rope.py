# python3

import sys
from functools import reduce

#import sys, threading
#sys.setrecursionlimit(10**7) # max depth of recursion
#threading.stack_size(2**25) # new thread will get stack of such size
class Stack(list):
    def push(self, item):
        self.append(item)
    def isEmpty(self):
        return not self

class Rope:
    def __init__(self, s):
        self.s = s
        lens = len(s)
        #vertices = map(NewVertex, range(lens))
        #list_indices = [Vertex(0, 1, None, None, None)]
        #list_indices.extend(range(lens))
        self.root = reduce(insert_special, range(1, lens), Vertex(0, 1, None, None, None))
        #self.printTree("init root : ", self.root)
    def result(self):
        return self.traverseTree(self.root)
    def getStr(self, cur_node):
        if (cur_node != None):
            return (self.s[cur_node.key:cur_node.key + cur_node.length] + ":" + str(cur_node.size))
        return ""
    def printNode(self, cur_node):
        str = self.getStr(cur_node) + "(" + self.getStr(cur_node.left) + ", " + self.getStr(cur_node.right) + ", " + self.getStr(cur_node.parent) + ")"
        print("node: " + str)
    def traverseTree(self, root, bVersbose = False):
        res = []
        node_stack = Stack()
        cur_node = root
        push = node_stack.push
        isEmpty = node_stack.isEmpty
        pop = node_stack.pop
        s = self.s
        append = res.append
        while (cur_node != None):
            push(cur_node)
            if bVersbose:
                self.printNode(cur_node)
            cur_node = cur_node.left
        while (not isEmpty()):
            cur_node = pop()
            first = cur_node.key
            #last = first + cur_node.length
            append(s[first])
            cur_node = cur_node.right
            while (cur_node != None):
                push(cur_node)
                #if bVersbose:
                #    self.printNode(cur_node)
                cur_node = cur_node.left
        return ''.join(res)
    def visit(self, cur_node):
        self.res.append(self.s[cur_node.key])
    def printTree(self, label, root, bVerbose = False):
        res = self.traverseTree(root, bVerbose)
        rootDetails = ""
        if (root != None) and bVerbose:
            rootDetails = str(root.key) + ":" + self.s[root.key:(root.key + root.length)]
        print(label, res, rootDetails)
    def process(self, i, j, k):
        # Write your code here
        self.splice(i, j, k)
    def splice(self, fr, to, bf):
        #print("frm to before", fr, to, bf)
        #self.printTree(root, "root: ")
        #(foundNode, root) = find(root, fr)

        (middle, right) = split(self.root, to + 1)
        #self.printTree("middle+left : ", middle)
        #self.printTree("right : ", right)

        (left, middle) = split(middle, fr)
        #self.printTree(left, "left : ")
        #self.printTree(middle, "middle : ")
        #left is left of fr, middle is s[fr..to], right is s[to+1..]

        #(left, middle) = split(self.root, fr)
        #self.printTree(left, "left : ")
        #self.printTree(middle, "middle+right: ")
        #(middle, right) = split(middle, to + 1 - fr)
        #self.printTree(middle, "middle : ")
        #self.printTree(right, "right : ")
        left = merge_special(left, right) #merge the left and right pieces
        #self.printTree(left, "left+right : ")

        (left, right) = split(left, bf) #split the recomined tree again, so we can insert the middle
        #self.printTree(left, "new left : ")

        middle = merge_special(left, middle)
        #self.printTree(middle, "new middle : ")

        self.root = merge_special(middle, right)
        #self.printTree("new root : ", self.root)


#we can use a splay tree to store the string and to cut and merge the pieces
#what'll be the key?    index position or the char?
#the char itself won't change when we re-arrange, so key must be current index
#position
#then we can use find() to find and split left, middle, right portions of
#string
#but after we split, the current index gets shifted left for the middle and
#right trees by the same constant for each tree
#so, perhaps we can just store/update this constant as a property of the root
#node only
#and when finding a key, we'll just subtract this constant from x, to map it to
#the index stored.

#N.size = N.left.size + N.right.size + 1
#well, when we use order statistics, we don't really care what the key is..
#so we can literally replace the key comparison (used in find)
#we'll change the update function to recompute size and not use key
#we'll change the find function to use the size attribute rather than the key
#attribute
#insert and erase also look at key
#so, scratch that, we won't change the find function, we'll just use a new
#orderStatistic function where we were using find.
#and let key be defined once (at the time of insertion) to be the original
#index of the character
#later, for printing, we'll use this index to retrieve the actual char from
#orig array
#but then, find will get screwed up after the first split and merge, since left
#subtree could have keys larger than right sub-tree!


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
    psize = parent.size
    vsize = v.size
    if parent.left == v:
        m = v.right
        v.right = parent
        parent.left = m
    else:
        m = v.left
        v.left = parent
        parent.right = m
    #update(parent)
    msize = 0
    if m != None:
        m.parent = parent
        msize = m.size
    parent.size = psize - vsize + msize
    #update(v)
    parent.parent = v
    v.size = psize
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
        smallRotation(v)
        smallRotation(v)

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

#assumes that we are guaranteed to find the index in the tree
#also note, we'll never have to revisit a node since indices will be unique
def findi(root, index_to_find):
    if root == None:
        return (root, root)
    if index_to_find >= root.size:
        return (None, root) #becuase we don't have an index as large in our tree
    #if index_to_find < 0:
    #    return None #because ours is a zero based index
    cur_node = root
    if cur_node.left != None:
        cur_index = cur_node.left.size
    else:
        cur_index = 0
    base_index = cur_index + 1 #will be used when we go right
    while cur_index != index_to_find:
        if index_to_find < cur_index: #go left!
            cur_node = cur_node.left #here .left will exist since inde_to_find is smaller than cur_index
        else: #go right!
            cur_node = cur_node.right #here .right will exist since inde_to_find is greater than cur_index
            index_to_find = index_to_find - cur_index - 1 #rebasing my index_to_find since i am moving right
        if cur_node == None:
            break
        if cur_node.left != None:
            cur_index = cur_node.left.size
        else:
            cur_index = 0
    #return cur_node
    newRoot = root
    if cur_node != None:
        newRoot = splay(cur_node)
    return (cur_node, newRoot)
#splits tree into left and right
#right tree root = key, if key was found in tree, else next bigger key becomes
#root of right tree
#root of left tree, is the left child of key (or nextv) after the key is
#splayed
#here, key is really the index at which to split
def split(root, key):
    (result, root) = findi(root, key)
    if result == None:
        #print("did not find index", key)
        return (root, None)
    #print("found index", key, ".    result is ", str(findIndex(result)),
    #str(result.key))
    #right = splay(result)
    right = result
    left = right.left
    right.left = None
    if left != None:
        left.parent = None
        right.size = right.size - left.size
    #update(left)
    #update(right)
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
    left.parent = right
    #update(right)
    right.size = right.size + left.size
    return right

#in our special case the root of the right node does not have a left child
def merge_special(left, right):
    if left == None:
        return right
    if right == None:
        return left
    #while right.left != None:
    #    right = right.left
    #right = splay(right)
    right.left = left
    left.parent = right
    #update(right)
    right.size = right.size + left.size
    return right
    
# Code that uses splay tree to solve the problem

#root = None
def insert(root, x):
    (left, right) = split(root, x)
    new_vertex = None
    if right == None or right.key != x:
        new_vertex = Vertex(x, x + 1, None, None, None)
    root = merge(merge(left, new_vertex), right)

def insert_special(root, x):
    new_vertex = Vertex(x, x + 1, root, None, None)
    root.parent = new_vertex
    return new_vertex

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
