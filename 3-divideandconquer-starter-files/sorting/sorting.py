# Uses python3
import sys
import random

def partition3_old(a, l, r):
    #write your code here
    x = a[l]
    j = l;
    m1 = m2 = l
    b_m1 = True
    print("orig a", a)
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            #j += 1
            while ((j < r) and (a[j] == x)):
                j += 1
                if b_m1:
                    m1 = j-1
                    b_m1 = False
            if (j <= r):
                a[i], a[j] = a[j], a[i]
            else:
                j = r
                break
    
    a[l], a[j] = a[j], a[l]
    
    if ( (b_m1) and (a[j] == x) ):
        m1 = j
    print ("a, x, m1, m2", a, x, m1, j)
    return (m1,j)

def partition3_old2(a, l, r):
    x = a[l]
    j = l;
    ax = []
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
            if (a[j] == x):
                ax.append(j)
    a[l], a[j] = a[j], a[l]
    #now j is the right most occurrence of x
    dups = len(ax)
    if ( (dups > 1) and (dups < j) ):
        #start swapping values to the left of j, so we get contiguous x
        for i in range(j-1, l, -1):
            pass
    return j


def partition3(a, l, r):
    x = a[l]
    j = l;
    m1 = r #indicates m1 has not been set to logical value
    b_m1 = True
    #print("orig a, l, r", a, l, r)
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
            #print ("after s1: a, m1, j", a, m1, j)
            if (m1 > j) and (a[j] == x):
                m1 = j
                b_m1 = False
            if (a[j] < x) and (m1 < j): #ensuring we have a contiguous sequence of elements that are equal to x
                a[j], a[m1] = a[m1], a[j]
                m1 += 1
                #print ("after s1: a, m1, j", a, m1, j)
    if (a[j] < x): #only swap the pivot with last point, if last point is strictly smaller than pivot
        a[l], a[j] = a[j], a[l]
    else: #else, we'll swap the pivot with something we know to be smaller
        if m1 < j: #only possible if m1 was set to logical value
            a[l], a[m1-1] = a[m1-1], a[l]
            m1 = m1 - 1
    #print ("a, x, m1, m2", a, x, m1, j)
    if m1 > j: #if at this point, we still have set m1, set it now
        m1 = j
    return (m1,j)



def partition2(a, l, r):
    x = a[l]
    j = l;
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    #m = partition2(a, l, r)
    m1,m2 = partition3(a, l, r)
    #print ("a, m1, m2", a, m1, m2)
    randomized_quick_sort(a, l, m1 - 1);
    randomized_quick_sort(a, m2 + 1, r);


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
