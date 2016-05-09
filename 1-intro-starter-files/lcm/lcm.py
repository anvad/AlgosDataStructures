# Uses python3
import sys

def lcm(a, b):
    #write your code here
    return int(a/gcdfast(a, b))*b

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

if __name__ == '__main__':
    input = sys.stdin.readline()
    a, b = map(int, input.split())
    print(lcm(a, b))

