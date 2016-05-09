# Uses python3
import sys

def get_fibonaccihuge(n, m):
    # write your code here
    #from https://en.wikipedia.org/wiki/Pisano_period
    #π(n) ≤ 6m,
    #so, we may need to calc the remainders for up to 12n digits to confirm the period
    startSeq = [0, 1] #each Pisano period starts with 01
    lenStart = len(startSeq)
    fibM = list(startSeq) #full sequence of remainders
    fibM1 = list(startSeq) #first sequence of remainders
    fibM2 = [] #second (confirming) sequence of remainders
    
    max = 2 * 6 * m + 3
    bCalcM2 = False
    for i in range(2,max):
        nextNum = (fibM[i-1] + fibM[i-2]) % m
        fibM.append( nextNum )
        
        if (bCalcM2): #implies we are creating 2nd seq
            fibM2.append( nextNum )
        else:
            fibM1.append( nextNum )
        #print(fibM)
        #print(fibM[-lenStart:])
        #print("fibM1= ", fibM1)
        if (fibM[-lenStart:] == startSeq): #checking if last few elements match starting sequence
            if (len(fibM2) > 0): #implies we are creating 3rd seq!
                fibM2 = fibM2[:-lenStart] #so, truncate last x element from 2nd seq to get final 2nd seq
                if fibM2 == fibM1:
                    #print("fibM1= ", fibM1)
                    break
                else:
                    #print("fibM1= ", fibM1)
                    #print("fibM2= ", fibM2)
                    pass
            else: #implies we are creating 2nd seq
                fibM1 = fibM1[:-lenStart] #so, truncate last x element from 1st seq to get final 1st seq
                fibM2 = list(startSeq)
                bCalcM2 = True
    #now we have the repeating sequence fibM1 (assumes fibM1 and fibM2 are equal)
    lenSeq = len(fibM1)
    fIndex = n % lenSeq
    return fibM1[fIndex]
        

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

if __name__ == '__main__':
    input = sys.stdin.readline();
    n, m = map(int, input.split())
    print(get_fibonaccihuge(n, m))
