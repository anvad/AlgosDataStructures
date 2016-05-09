# Uses python3
import sys

def gcd(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd

def gcdfast(a, b):
    m = a
    n = b
    if (a > b):
        m = b
        n = a
    #so, at this time, we've stored
        #the larger number in m
        #and smaller number in n
    #now, we'll iteratively calculate newer values of m and n, till n reaches 0.
    while (n > 0):
        new_m = n #this line is computationally redundant, but makes it easier to understand
        new_n = m % n
        m = new_m
        n = new_n
    return m

if __name__ == "__main__":
    input = sys.stdin.readline()
    a, b = map(int, input.split())
    #print(gcd(a, b))
    print(gcdfast(a, b))
