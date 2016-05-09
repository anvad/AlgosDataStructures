# Uses python3
import sys

def get_majority_element_adv(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    #write your code here
    c = {}
    half = n/2
    for i in range(right):
        if a[i] in c:
            c[a[i]] += 1
        else:
            c[a[i]] = 1
        if c[a[i]] > half:
            return a[i]
    return -1

def get_count(a, ME):
    count = 0
    max = len(a)
    for i in range(max):
        #print("a[i],ME= ",a[i],ME)
        if ( a[i] == ME ):
            count += 1
    #print("count= ", count)
    return count
def get_majority_element(a, left, right):
    #print(a, left, right)
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    #write your code here
    mid = left + int((right - left)/2)
    MEL = get_majority_element(a, left, mid)
    #print("MEL= ",MEL)
    if MEL > -1:
        count = get_count(a[left:right], MEL)
        #print("MEL Count= ", count)
        if count > (right - left)/2:
            return MEL
    MER = get_majority_element(a, mid, right)
    #print("MER= ",MER)
    if MER > -1:
        count = get_count(a[left:right], MER)
        #print("MER Count= ", count)
        if count > (right - left)/2:
            return MER
    return -1

def get_majority_element_faster(a, left, right): #calls get_count on only half as many elements
    #print(a, left, right)
    if left == right:
        return (-1, 0)
    if left + 1 == right:
        return (a[left], 1)
    #write your code here
    mid = left + int((right - left)/2)
    (MEL,cL) = get_majority_element_faster(a, left, mid)
    #print("MEL= ",MEL)
    if MEL > -1:
        cR = get_count(a[mid:right], MEL)
        count = cL + cR
        #print("MEL Count= ", count)
        if count > (right - left)/2:
            return (MEL, count)
    (MER,cR) = get_majority_element_faster(a, mid, right)
    #print("MER= ",MER)
    if MER > -1:
        cL = get_count(a[left:mid], MER)
        count = cL + cR
        #print("MER Count= ", count)
        if count > (right - left)/2:
            return (MER, count)
    return (-1, 0)
if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    (ME, count) = get_majority_element_faster(a, 0, n)
    if ME != -1:
        print(1)
    else:
        print(0)
