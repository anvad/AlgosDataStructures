# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size

class Node:
    def __init__(self, key):
        self.key = key
        self.children = []
        #self.parent = parent
    def add_child(self, child):
        self.children.append(child)
    
class TreeHeight:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.parent = list(map(int, sys.stdin.readline().split()))

    def traverse_tree(self, node_index, nodes):
        node_children = nodes[node_index]
        if len(node_children)==0:
            return 1
        maxHeight = 0
        for child_index in node_children:
            height = 1 + self.traverse_tree(child_index, nodes)
            maxHeight = max(maxHeight, height);
        return maxHeight

    def compute_height(self):
        # Replace this code with a faster implementation

        #existing algo is traversing path to the root, for each element in the tree, so we'll visit the same node multiple times            
##        maxHeight = 0
##        for vertex in range(self.n):
##            height = 0
##            i = vertex
##            while i != -1:
##                height += 1
##                i = self.parent[i]
##                maxHeight = max(maxHeight, height);
##        return maxHeight;

        #if we do BFS or DFS, we'll visit each node just once
        maxHeight = 0
        nodes = {} #key is key of node, value is list of children of node
        #root_node = Node()
        for i,parent_vertex in enumerate(self.parent):
            if i not in nodes:
                nodes[i] = []
            if parent_vertex == -1:
                root_node = i
            else:
                if parent_vertex not in nodes:
                    nodes[parent_vertex] = []
                nodes[parent_vertex].append(i) #since ith node is a child of parent_vertex

        #now to traverse the tree
        maxHeight = self.traverse_tree(root_node, nodes)
        return maxHeight;
        
        

def main():
  tree = TreeHeight()
  tree.read()
  print(tree.compute_height())

threading.Thread(target=main).start()
