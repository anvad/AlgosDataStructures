# Uses python3
import sys
import random

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

#find number of elements that are less than or equal to x
#'a' is a sorted array
def find_num_smaller(a, x):
    left, right = 0, len(a)
    max = right
    # write your code here
    while ( left < (right - 1) ):
        i = left + (right - left)//2
        #print("1 a[left:right]",a[left:right])
        #print ("l=",left,"i=",i,"r=",right)
        if a[i] == x:
            #now check higher indices
            #print("found match.  max, i, a[i], x ", max, i, a[i], x)
            while (i < max) and a[i] == x:
                i += 1
            #print("found max i.  max, i, a[i], x ", max, i, a[i], x)
            return i
        elif a[i] < x:
            left = i
        else:
            right = i
        #print("2 a[left:right]",a[left:right],"\n")
    #if i am here, it means i did not find exact match. a[left:right] will contain just 1 element which is the smallest index, or the largest element smaller than x
    #if this element index is 0, return 0, since this implies x is smaller than the smallest element
    #if this last element is >0, return the next index up, as that would be the number of elements less than or equal to x
    #print("a[left:right], i, a[i], x, a[i+1]", a[left:right], i, a[i], x)
    if left == 0:
        return left
    return right

def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    #write your code here

    #first sort starts and ends in ascending order
    #sorted_starts = starts[:] #time exceeded. Copying array taking too long!
    sorted_starts = starts #so instead of copying to it, just pointing to it, as i don't really need to preserve orig array
    #sorted_ends = ends[:]
    sorted_ends = ends

    randomized_quick_sort(sorted_starts, 0, len(sorted_starts))
    randomized_quick_sort(sorted_ends, 0, len(sorted_starts))
    

    #then loop thru each point and find cnt
    i = 0
    for p in points:
        #binary search sorted_starts to find number of starting points smaller than p (s_cnt)
        #binary search sorted_ends to find number of ending points smaller than p (e_cnt)
        #cnt = s_snt - e_cnt
        s_cnt = find_num_smaller(sorted_starts, p)
        e_cnt = find_num_smaller(sorted_ends, p)
        cnt[i] = s_cnt - e_cnt
        i += 1
    return cnt

def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    #use fast_count_segments
    cnt = naive_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')
