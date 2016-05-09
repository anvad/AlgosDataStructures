# python3

import sys

class Rope:
  def __init__(self, s):
    self.s = s
    lens = len(s)
    #for i in range(lens):
    #  #print(i, s[i], sep=":", end=" ")
    #  insert(i)
    #print("")
    #print(self.result())
  def result(self):
    return ''.join(self.s)
  def process(self, i, j, k):
    # Write your code here
    remainingString = self.s[0:i] + self.s[j+1:]
    middleString = self.s[i:j+1]
    self.s = remainingString[0:k] + middleString + remainingString[k:]
rope = Rope(sys.stdin.readline().strip())
q = int(sys.stdin.readline())
for _ in range(q):
  i, j, k = map(int, sys.stdin.readline().strip().split())
  rope.process(i, j, k)
print(rope.result())
#rope.PrintResult()
