# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    TotalValue = 0.
    dvw = []
    fracWeights = []
    # write your code here
    for w, v in zip(weights, values):
        if w > 0:
            density = v/w
        else:
            density = 0
        dvw.append((density, v, w))
        fracWeights.append(0)
    dvw.sort(reverse=True)
    
    #print("dvw ", dvw)
    #print("weights ", weights)
    #print("values ", values)

    i = 0
    for (density, value, weight) in dvw:
        w = min(weight, capacity)
        TotalValue = TotalValue + w * density
        fracWeights[i] = w
        i = i + 1
        capacity = capacity - w
        if capacity == 0:
            break
    #print("fracWeights ", fracWeights)
    return TotalValue



if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
