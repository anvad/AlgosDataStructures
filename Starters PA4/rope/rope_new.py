# python3

import sys

class Stack(list):
    def push(self, item):
        self.append(item)
    def isEmpty(self):
        return not self
# Vertex of a splay tree
class Vertex:
    def __init__(self, key, size, length, left, right, parent):
        #key stores the first index of sub-string stored in this vertex
        #last stores 1 + last index of sub-string stored in this vertex
        (self.key, self.size, self.length, self.left, self.right, self.parent) = (key, size, length, left, right, parent)

class Rope:
    def __init__(self, s):
        self.s = s
        self.root = Vertex(0, len(s), len(s), None, None, None)
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
        append = res.append
        while (cur_node != None):
            push(cur_node)
            if bVersbose:
                self.printNode(cur_node)
            cur_node = cur_node.left
        while (not isEmpty()):
            cur_node = pop()
            first = cur_node.key 
            last = first + cur_node.length
            append(self.s[first:last])
            cur_node = cur_node.right
            while (cur_node != None):
                push(cur_node)
                #if bVersbose:
                #    self.printNode(cur_node)
                cur_node = cur_node.left
        return ''.join(res)
    def printTree(self, label, root, bVerbose = False):
        res = self.traverseTree(root, bVerbose)
        rootDetails = ""
        if (root != None):
            rootDetails = str(root.key) + ":" + self.s[root.key:(root.key + root.length)]
        print(label, res, rootDetails)
    def process(self, i, j, k):
        (middle, right) = split(self.root, j+1)
        #self.printTree("middle+left : ", middle, True)

        (left, middle) = split(middle, i)
        #self.printTree("left        : ", left, True)
        #self.printTree("middle      : ", middle, True)

        left = merge(left, right) #merge the left and right pieces
        #self.printTree("left+right  : ", left, True)

        (left, right) = split(left, k) #split the recomined tree again, so we can insert the middle
        #self.printTree("new left    : ", left, True)

        middle = merge(left, middle)
        #self.printTree("new middle  : ", middle, True)

        self.root = merge(middle, right)
        #self.printTree("new root    : ", self.root, True)
        #print("-------------------------------------------------")

#all tree related operations
def update(v):
    if v == None:
        return
    v.size = v.length
    if v.left != None:
        v.left.parent = v
        v.size = v.size + v.left.size
    if v.right != None:
        v.right.parent = v
        v.size = v.size + v.right.size

def smallRotation(v):
    parent = v.parent
    if parent == None:
        return
    grandparent = v.parent.parent
    psize = parent.size
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
    #parent.parent = v
    #v.size = psize
    v.parent = grandparent
    if grandparent != None:
        if grandparent.left == parent:
            grandparent.left = v
        else:
            grandparent.right = v

def bigRotation(v):
    #parent = v.parent
    #grandparent = parent.parent
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

def findNextIndex(root, index_to_find):
    #print("index_to_find orig", index_to_find)
    if root == None:
        return (root, 0)
    if index_to_find > root.size:
        #print("index_to_find larger than size", index_to_find, root.size)
        return (None, 0) #this would happen when we are trying to append/insert something to our tree, so nextv would be None
    index_to_find_orig = index_to_find
    cur_node = root
    if cur_node.left != None:
        cur_index = cur_node.left.size
    else:
        cur_index = 0
    cur_last = cur_index + cur_node.length
    isSmaller = index_to_find < cur_index
    isLarger = index_to_find >= cur_last
    while isSmaller or isLarger: #while curent node does not contain the index
        #print("index_to_find, cur_index, cur_last", index_to_find, cur_index)
        if isSmaller: #go left!
            cur_node = cur_node.left #here .left will exist since inde_to_find is smaller than cur_index
        else: #index_to_find > cur_index: #go right!
            cur_node = cur_node.right #here .right will exist since inde_to_find is greater than cur_index
            index_to_find = index_to_find - cur_last #rebasing my index_to_find since i am moving right
        if (cur_node == None):
            print("should not have happened but ran out of tree! index_to_find_orig, cur_index, index_to_find, cur_last", index_to_find_orig, cur_index, index_to_find, cur_last)
            cur_index = index_to_find
            break
        if cur_node.left != None:
            cur_index = cur_node.left.size
        else:
            cur_index = 0
        cur_last = cur_index + cur_node.length
        isSmaller = index_to_find < cur_index
        isLarger = index_to_find >= cur_last
    index_in_node = index_to_find - cur_index
    return (cur_node, index_in_node)

#splits tree into left and right
#right tree root = key, if key was found in tree, else next bigger key becomes root of right tree
#root of left tree, is the left child of key (or nextv) after the key is splayed
#here, key is really the index at which to split
def split(root, split_at_index):
    (node_found, index_in_node) = findNextIndex(root, split_at_index)
    if node_found == None:
        ##print("did not find index", key)
        return (root, None)
    else:
        new_root = splay(node_found)
        #now getting ready to split the node
        if index_in_node > 0:
            #save some properties of the new root
            right_child = new_root.right
            treesize = new_root.size
            rootlength = new_root.length

            #now update left tree
            node_left = new_root
            node_left.length = index_in_node
            node_left.right = None
            node_left.parent = None
            nlsize = index_in_node + (node_left.left.size if node_left.left != None else 0)
            node_left.size = nlsize

            #creating node_right and updating its attributes
            new_length = rootlength - index_in_node
            node_right = Vertex(new_root.key + index_in_node, treesize - nlsize, new_length, None, right_child, None)
            if right_child != None:
                right_child.parent = node_right

        else:
            node_left = new_root.left
            nlsize = 0
            if node_left != None:
                node_left.parent = None
                nlsize = node_left.size
            node_right = new_root
            node_right.left = None
            node_right.size = node_right.size - nlsize
        return (node_left, node_right)

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
    right.size = right.size + left.size
    #update(right)
    return right

rope = Rope(sys.stdin.readline().strip())
q = int(sys.stdin.readline())
for _ in range(q):
    i, j, k = map(int, sys.stdin.readline().strip().split())
    rope.process(i, j, k)
print(rope.result())
