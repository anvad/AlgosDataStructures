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
    def traverseTree(self, root):
        res = []
        node_stack = Stack()
        cur_node = root
        while (cur_node != None):
            node_stack.push(cur_node)
            cur_node = cur_node.left
        while (not node_stack.isEmpty()):
            cur_node = node_stack.pop()
            last = cur_node.key + cur_node.length
            res.append(self.s[cur_node.key:last])
            cur_node = cur_node.right
            while (cur_node != None):
                node_stack.push(cur_node)
                cur_node = cur_node.left
        return ''.join(res)
    def printTree(self, label, root):
        res = self.traverseTree(root)
        rootDetails = ""
        if (root != None):
            rootDetails = str(root.key) + ":" + self.s[root.key:(root.key + root.length)]
        print(label, res, rootDetails)
    def process(self, i, j, k):
        (middle, right) = self.split(self.root, j+1)
        self.printTree("middle+left : ", middle)

        (left, middle) = self.split(middle, i)
        self.printTree("left        : ", left)
        self.printTree("middle      : ", middle)

        left = self.merge(left, right) #merge the left and right pieces
        self.printTree("left+right  : ", left)

        (left, right) = self.split(left, k) #split the recomined tree again, so we can insert the middle
        self.printTree("new left    : ", left)

        middle = self.merge(left, middle)
        self.printTree("new middle  : ", middle)

        self.root = self.merge(middle, right)
        self.printTree("new root    : ", self.root)

    #all tree related operations
    def update(self, v):
        if v == None:
            return
        v.size = v.length + (v.left.size if v.left != None else 0) + (v.right.size if v.right != None else 0)
        if v.left != None:
            v.left.parent = v
        if v.right != None:
            v.right.parent = v

    def smallRotation(self, v):
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
        self.update(parent)
        self.update(v)
        v.parent = grandparent
        if grandparent != None:
            if grandparent.left == parent:
                grandparent.left = v
            else:
                grandparent.right = v

    def bigRotation(self, v):
        if v.parent.left == v and v.parent.parent.left == v.parent:
            # Zig-zig
            self.smallRotation(v.parent)
            self.smallRotation(v)
        elif v.parent.right == v and v.parent.parent.right == v.parent:
            # Zig-zig
            self.smallRotation(v.parent)
            self.smallRotation(v)
        else:
            # Zig-zag
            self.smallRotation(v)
            self.smallRotation(v)

    # Makes splay of the given vertex and makes
    # it the new root.
    def splay(self, v):
        if v == None:
            return None
        while v.parent != None:
            if v.parent.parent == None:
                self.smallRotation(v)
                break
            self.bigRotation(v)
        return v

    def findNextIndex(self, root, index_to_find):
        if root == None:
            return (root, 0)
        if index_to_find > root.size:
            print("index_to_find larger than size", index_to_find, root.size)
            return (None, 0) #this would happen when we are trying to append/insert something to our tree, so nextv would be None
        cur_node = root
        if (cur_node.left != None):
            cur_index = cur_node.left.size
        else:
            cur_index = 0
        cur_last = cur_index + cur_node.length
        while (index_to_find < cur_index) or (index_to_find > cur_last): #while curent node does not contain the index
            if (index_to_find < cur_index): #go left!
                cur_node = cur_node.left #here .left will exist since inde_to_find is smaller than cur_index
            if index_to_find > cur_index: #go right!
                cur_node = cur_node.right #here .right will exist since inde_to_find is greater than cur_index
                index_to_find = index_to_find - cur_index - cur_node.length #rebasing my index_to_find since i am moving right
            cur_last = cur_node.key + cur_node.length
            if (cur_node.left != None):
                cur_index = cur_node.left.size
            else:
                cur_index = 0
            cur_last = cur_index + cur_node.length
        index_in_node = index_to_find - cur_index
        if index_in_node > 0:
            print("splitting node", self.s[cur_node.key:(cur_node.key + cur_node.length)], "->", self.s[index_in_node:(cur_node.key + cur_node.length)])
        else:
            print("not splitting node", self.s[cur_node.key:(cur_node.key + cur_node.length)], "index_in_node= ", index_in_node)
        return (cur_node, index_in_node)

    def find(self, root, index_to_find):
        (node_found, index_in_node) = self.findNextIndex(root, index_to_find)
        new_root = root
        if (node_found != None):
            new_root = self.splay(node_found)
        #now getting ready to split the node
        if index_in_node > 0:
            node_left = node_found
            new_length = node_left.length - index_in_node
            node_found = Vertex(node_left.key + index_in_node, node_left.size + new_length, new_length, node_left, node_left.right, None)
            new_root = node_found
            node_left.length = index_in_node
            node_left.size = node_left.size - index_in_node
            node_left.parent = node_found
            node_left.right = None
        return (node_found, new_root)

    #splits tree into left and right
    #right tree root = key, if key was found in tree, else next bigger key becomes root of right tree
    #root of left tree, is the left child of key (or nextv) after the key is splayed
    #here, key is really the index at which to split
    def split(self, root, key):
        (result, root) = self.find(root, key)
        if result == None:
            #print("did not find index", key)
            return (root, None)
        #print("found index", key, ". result is ", str(findIndex(result)), str(result.key))
        right = self.splay(result)
        left = right.left
        #now here, my left's root has correct index, but if left's root has right side children
        right.left = None
        if left != None:
            left.parent = None
        self.update(left)
        self.update(right)
        return (left, right)

    #this assumes left and right tree don't overlap
    #find the left-most node in right tree
    #splay it, so it becomes root
    #obviously this node will not have a left child
    #so, simply attach the left tree as a child of the right tree
    def merge(self, left, right):
        if left == None:
            return right
        if right == None:
            return left
        while right.left != None:
            right = right.left
        right = self.splay(right)
        right.left = left
        self.update(right)
        return right

rope = Rope(sys.stdin.readline().strip())
q = int(sys.stdin.readline())
for _ in range(q):
    i, j, k = map(int, sys.stdin.readline().strip().split())
    rope.process(i, j, k)
print(rope.result())