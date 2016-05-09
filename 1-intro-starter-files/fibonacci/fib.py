# Uses python3
def calc_fib(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)

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

n = int(input())
#print(calc_fib(n))
print(calc_fib_iter(n))
