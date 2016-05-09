# Uses python3
import sys

def optimal_sequence_orig(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence)


#n -> W, (a0,k0,...ai,opi,...ak-1,opk-1) -> (vi, wi)
#non repeating
#optimal soln is a seq of ai... so set of possible ai = 1, 2, 3, ... n - ak-1
#so, removing n, leads us to the optimal soln to get to ak-1. Now, ak-1 could be equal to n-1, or n/2 or n/3. The exact operation = opk-1
#let fn that computes the optimal seq be - optimal_seq
#then, optimal_seq(n) = optimal_seq(ak-1).append(ak-1,opk-1)
#so, i could calc optimal_seq of every number from 0 to n. that's a lot!
#C(n) = optimal number of ops to get to n, from 1
#so, taking last operation out, i.e. C(n) -1, the last number in seq would be n-1, or n/2 or n/3. and one of C(n-1), c(n/2) or C(n/3) is smallest!
#so, C(n) = min{ c(n-1), c(n/2), c(n/3) } + 1
#and C(0) = 1, C(1) = 0
#if n/2 is not whole, then c(n/2) is not possible, so this number is infinity
#similarly for c(n/3) if n/3 is not whole
#C[0] = 1
#C[1] = 0
#C[n+1] = n + 2 #+ve infinity
#for i from 1 to n:
#   a = n + 1
#   b = n + 1
#   if i % 2 == 0:
#       a = C[i/2]
#   if i % 3 == 0:
#       b = C[i/2]
#   c = C[i - 1]
#   C[i] = min(

def optimal_sequence_too_much_mem(n):
    #C = [[0]]*n #C is a list of lists, or an array of arrays
    C = []
    max = [0] * n
    C.append([0])
    #C[1] = [1]
    C.append([1])
    #print(C)
    if n < 2:
        return C[n]
    for i in range(2, n+1):
        a = max
        b = max
        if i % 2 == 0:
            a = C[i//2]
        if i % 3 == 0:
            b = C[i//3]
        c = C[i-1]
        d = min(a, b, c, key=len)
        d_clone = d[:]
        d_clone.append(i)
        C.append(d_clone)
        #print(i, a, b, c, d_clone)

    #now to get the sequence
    return C[n]

#104MB, 2.16 secs
def optimal_sequence_still_too_much_mem(n):
    #C = [[0]]*n #C is a list of tuples
    #C[n] contains num_ops,ak-1, assuming a0,a1,...ak-1,n is the seq and a0 = 1
    C = [(0,0), (0,1)] #so, C[1] = 0,1, i.e. num_ops = 0, and previous number = 1
    if n < 2:
        return [1]
    for i in range(2, n+1):
        a1 = b1 = n
        c1 = i-1
        a = n + 1, a1 #initialzing a and b
        b = n + 1, b1 #initialzing a and b
        if i % 2 == 0:
            a1 = i//2
            a = C[a1][0] + 1, a1
        if i % 3 == 0:
            b1 = i//3
            b = C[b1][0] + 1, b1
        c = C[c1][0] + 1, c1
        d = min(a, b, c)
        C.append(d)
        #print(i, a, b, c, d)

    #now to get the sequence
    #seq = [0] * (n + 1)
    #seq[n] =
    print(C)
    seq = [n]
    i = n
    while i > 1:
        i = C[i][1]
        seq.append(i)
    #seq.append(n)
    return reversed(seq)

#73MB, 1.83 secs
def optimal_sequence_still_too_much_mem(n):
    #C = [[0]]*n #C is a list of tuples
    #C[n] contains num_ops,opk assuming a0,a1,...ak-1,n is the seq and a0 = 1, op1 is the operation to get from 0 to 1
    #op = 0 implies +1, 1 -> *2, 2 -> *3
    C = [(0,0), (0,1)] #so, C[1] = 0,1, i.e. num_ops = 0, and previous number = 1
    if n < 2:
        return [1]
    for i in range(2, n+1):
        a1 = b1 = n
        c1 = i-1
        a = n + 1, a1 #initialzing a and b
        b = n + 1, b1 #initialzing a and b
        if i % 2 == 0:
            a1 = i//2
            a = C[a1][0] + 1, 1 #since op is *2
        if i % 3 == 0:
            b1 = i//3
            b = C[b1][0] + 1, 2 #since op is *3
        c = C[c1][0] + 1, 0 #since op is +1
        d = min(a, b, c)
        C.append(d)
        #print(i, a, b, c, d)

    #now to get the sequence
    #seq = [0] * (n + 1)
    #seq[n] =
    #print(C)
    seq = [n]
    i = n
    while i > 1:
        op = C[i][1]
        if op == 0:
            i = i - 1
        elif op == 1:
            i = i // 2
        else:
            i = i // 3
        seq.append(i)
    #seq.append(n)
    return reversed(seq)

#21MB, 1.97 secs
#so, using two separate lists takes much less memory than using 1 list with a 2 node tuple
def optimal_sequence(n):
    #C = [[0]]*n #C is a list of tuples
    #C[n] contains num_ops,opk assuming a0,a1,...ak-1,n is the seq and a0 = 1, op1 is the operation to get from 0 to 1
    #op = 0 implies +1, 1 -> *2, 2 -> *3
    num_ops = [0, 0] #so, C[1] = 0,1, i.e. num_ops = 0, and previous number = 1
    seq_ops = [0, 1]
    if n < 2:
        return [1]
    for i in range(2, n+1):
        a1 = b1 = n
        c1 = i-1
        a = n + 1, 1 #initialzing a and b
        b = n + 1, 2 #initialzing a and b
        if i % 2 == 0:
            a1 = i//2
            a = num_ops[a1] + 1, 1 #since op is *2
        if i % 3 == 0:
            b1 = i//3
            b = num_ops[b1] + 1, 2 #since op is *3
        c = num_ops[c1] + 1, 0 #since op is +1
        d = min(a, b, c)
        num_ops.append(d[0]) #here, instead of storing d tuple in one list, i am splitting and storing each element in its own list
        seq_ops.append(d[1])
        #print(i, a, b, c, d)

    #now to get the sequence
    #seq = [0] * (n + 1)
    #seq[n] =
    #print(C)
    seq = [n]
    i = n
    while i > 1:
        op = seq_ops[i]
        if op == 0:
            i = i - 1
        elif op == 1:
            i = i // 2
        else:
            i = i // 3
        seq.append(i)
    #seq.append(n)
    return reversed(seq)



input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
