# python3

import sys
from functools import reduce

# Vertex of a splay tree
class Vertex:
    def __init__(self, key, size, left, right, parent):
        (self.key, self.size, self.left, self.right, self.parent) = (key, size, left, right, parent)


class Rope:
    def __init__(self, s):
        self.s = s
        lens = len(s)
        #vertices = map(NewVertex, range(lens))
        #list_indices = [Vertex(0, 1, None, None, None)]
        #list_indices.extend(range(lens))
        self.root = reduce(insert_special, range(1, lens), Vertex(0, 1, None, None, None))
        #self.printTree("init root : ", self.root)

def insert_special(root, x):
    new_vertex = Vertex(x, x + 1, root, None, None)
    root.parent = new_vertex
    return new_vertex

s = sys.stdin.readline()
rope = Rope(s)
print(s)