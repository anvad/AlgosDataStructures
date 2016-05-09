# Uses python3
import sys

def optimal_summands(n):
    summands = []
    #write your code here
    ai = 1
    while n > 0:
        #print("ai, n ", ai, n)
        if n/2 <= ai:
            ai = n
        summands.append(ai)
        n = n - ai
        ai = ai + 1
    return summands

if __name__ == '__main__':
    input = sys.stdin.readline()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
