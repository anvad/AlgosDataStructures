# Uses python3
import sys

def optimal_weight(W, w):
    # write your code here
    n = len(w)
    result = 0
    value = []
    for i in range(0,n+1):
        value.append([0])
        for j in range(W):
            value[i].append(0)
    for i in range(1,n+1):
        for weight in range(1, W+1):
            value[i][weight] = value[i-1][weight]
            #print(n, i)
            if w[i-1] <= weight:
                val = value[i-1][weight - w[i-1]] + w[i-1]
                if val > value[i][weight]:
                    value[i][weight] = val
    return value[len(w)][W]

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
