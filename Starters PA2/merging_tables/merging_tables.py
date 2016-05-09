# python3

import sys

n, m = map(int, sys.stdin.readline().split())
rows = list(map(int, sys.stdin.readline().split()))
rank = [0] * n
parent = list(range(0, n))
ans = max(rows)

def getParent(table):
    # find parent and compress path
    intermediate_nodes = []
    #find root
    while parent[table] != table:
        intermediate_nodes.append(table)
        table = parent[table]
    root = table
    #now compress table
    for table in intermediate_nodes:
        parent[table] = root
    return root

def merge(destination, source):
    #print(ans)
    global ans
    realDestination = getParent(destination)
    realSource = getParent(source)

    if realDestination == realSource:
        return False

    # merge two components
    # use union by rank heuristic 
    # update ans with the new maximum table size

    #we can't really use rank heuristics since we've been explicitly told to copy from src to dst irrespective of rank!
    rows[realDestination] += rows[realSource]
    if rows[realDestination] > ans:
        ans = rows[realDestination]
    rows[realSource] = 0
    parent[realSource] = realDestination
    return True

for i in range(m):
    destination, source = map(int, sys.stdin.readline().split())
    #print(ans)
    merge(destination - 1, source - 1)
    print(ans)
    
