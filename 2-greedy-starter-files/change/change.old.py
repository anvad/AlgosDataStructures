# Uses python3
import sys

def get_change(n):
    #write your code here
    CVals = [10, 5, 1]
    CNums = [0, 0, 0]
    V = 0 #contains total value of coins, so far
    iMax = len(CVals)
    newN = n
    for i in range(len(CVals) + 1):
        CNums[i] = int(newN/CVals[i])
        newN = newN - CNums[i] * CVals[i]
        V = V + CNums[i]
        if newN <= 0:
            break
    #print(CNums)
    return V

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    print(get_change(n))
