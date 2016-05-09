# Uses python3
import sys

def merge(a, d, left, right, ave): #here, right is one index out of range
    leftB = left #iterates over "B" (i.e. left) array
    leftC = ave #iterates over "C" (i.e. right) array
    leftD = left #iterates over "D" (i.e. sorted) array
    #d = []
    #print("a=", a)
    #print("d=", d)
    #print("left, ave, right", left, ave, right)
    num_inversions = 0

    #now start filling up array D, from left to right in ascending order
    #stop when you run out of elements in array B or C
    while (leftB < ave) and (leftC < right): #here, right is one index out of range, hence not using <= operators
        bi = a[leftB]
        ci = a[leftC]
        #print("leftB, leftC, leftD, bi, ci", leftB, leftC, leftD, bi, ci)
        if (bi <= ci):
            d[leftD] = bi
            leftB += 1
        else:
            d[leftD] = ci
            leftC += 1
            num_inversions += ave - leftB #i.e. all the remaining elements in array "B"
            #print("num_inv= ", ave - leftB)
        leftD += 1
    if leftB < ave:
        #d[leftD:ave-leftB] = a[leftB:ave] #no need to copy these remaining elements to D, as they waste time and do not help in calc num_inversions, nor in sorting A
        a[leftD:right] = a[leftB:ave] #copying the rightmost sorted elements from B, back to A
    #if leftC < right:
        #d[leftD:right-leftC] = a[leftC:right] #no need to copy these remaining elements to D, as they waste time and do not help in calc num_inversions, nor in sorting A
        #a[leftD:right] = a[leftC:right] #no need to copy rightmost elements from C to A, as they are already in place in A, i.e. leftD = leftC if leftB is not < ave
        #pass #no need to copy rightmost elements from C to A, as they are already in place in A
    a[left:leftD] = d[left:leftD] #irrespective of whether B or C array has left-over elements, we have to copy the left most elements back to A
    #a[left:right] = d[left:right] #finally copying ALL the sorted elements back to A. this is repetitive and hence failing time constraint,
    #                               so instead copying only necessary elements back into a, instead of all sorted elements
    return num_inversions

def get_number_of_inversions(a, b, left, right): #here, right is one index out of range
    number_of_inversions = 0
    if right - left <= 1:
        return number_of_inversions
    ave = (left + right) // 2
    number_of_inversions += get_number_of_inversions(a, b, left, ave)
    number_of_inversions += get_number_of_inversions(a, b, ave, right)
    #write your code here
    number_of_inversions += merge(a, b, left, right, ave)
    return number_of_inversions

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    print(get_number_of_inversions(a, b, 0, len(a))) 
