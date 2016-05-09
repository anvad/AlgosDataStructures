# Uses python3
import sys

def get_fibonacci_last_digit(n):
    # write your code here
    if (n <= 1):
        return n
    m = n + 1
    fibLast = []
    fibLast.append(0)
    fibLast.append(1)
    for i in range(2,m):
        #fibLast.append( (fibLast[i-1] % 10) + (fibLast[i-2] % 10) )
        fibLast.append( (fibLast[i-1] + fibLast[i-2]) % 10 )

    return fibLast[n]

def calc_fib_iter(n):
    if (n <= 1):
        return n
    m = n + 1
    fib = []
    fib.append(0)
    fib.append(1)
    for i in range(2,m):
        fib.append(fib[i-1] + fib[i-2])

    return fib[n]

if __name__ == '__main__':
    input = sys.stdin.readline()
    n = int(input)
    print(get_fibonacci_last_digit(n))
