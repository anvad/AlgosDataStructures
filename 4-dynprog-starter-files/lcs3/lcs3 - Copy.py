#Uses python3

import sys

#now i am finally inside memory limits!
#taking 20 secs though, whereas the limit is only 10
#so how to reduce compute time?
def lcs3_slow_small(a1, b1, c1): #also prints each lcs
    (c_max,c),(b_max,b),(a_max,a) = sorted([(len(a1),a1), (len(b1),b1), (len(c1),c1)])
    #print(a_max,a)
    #print(b_max,b)
    #print(c_max,c)
    #now, i've made sure "a" is the largest sequence. This minimizes the memory needed to store seqs

    len_lcs = []
    seqs = [] #list of actual lcs, now storing only 1 level deep
    seqs2 = [] #contains 2 row of sequences from diagonal line in lower level and for current line in lower level
    set_seqs = set() #making sure we are not repeating any sequence in seqs[i][j][k]
    #creating elements of seqs ahead of time
    for j in range(b_max + 1):
        seqs.append([]) #for each j, create 2nd list
        for k in range(c_max + 1):
            seqs[j].append([]) #for each k, creating 3rd list
    for j in range(2):
        seqs2.append([]) #for each j, create 2nd list
        for k in range(c_max + 1):
            seqs2[j].append([]) #for each k, creating 3rd list

    for i in range(a_max + 1):
        len_lcs.append([]) #for each i, create 2nd list
        for j in range(b_max + 1):
            len_lcs[i].append([]) #for each j, create 3rd list
            j2 = j%2
            for k in range(c_max + 1):
                #print("i,j,k", i, j, k)
                seqs2[j2][k] = seqs[j][k] #save current spot
                if (i == 0) or (j==0) or (k==0):
                    len_lcs[i][j].append(0) #setting all boundary points to null. "n" denotes null
                    #seqs[i2][j][k] = [()] #setting all boundary points to list containing empty tuple
                    seqs[j][k] = [[]] #setting all boundary points to list containing empty list
                else: #it means none of the indices are 0, so we are dealing with inside points
                    if (a[i-1]==b[j-1]) and (a[i-1]==c[k-1]): #using -1 since a,b,c are zero based
                        lcs_max = len_lcs[i-1][j-1][k-1] + 1 #since last element in each sequence matches, the len_lcs is 1 + len_lcs of the slightly smaller subsequences
                        seqs[j][k] = [] #reset seqs for current indices
                        for l in seqs2[j2-1][k-1]: #now add the lcs values from smaller subsequences, appending this element to each
                            #ltemp = l[:]
                            #ltemp.append(a[i-1])
                            ltemp = l + [a[i-1]]
                            seqs[j][k].append(ltemp)
                            #print("l, ltemp",l, ltemp)
                        #print("seqs[i][j][k]", i, j, k, seqs[i2][j%2][k%2])
                    else:
                        p1 = len_lcs[i-1][j][k]
                        p2 = len_lcs[i][j-1][k]
                        p3 = len_lcs[i][j][k-1]
                        p4 = len_lcs[i][j-1][k-1]
                        p5 = len_lcs[i-1][j][k-1]
                        p6 = len_lcs[i-1][j-1][k]
                        lcs_max = max(p1, p2, p3, p4, p5, p6)
                        seqs[j][k] = [] #reset seqs for current indices
                        #set_seqs = set() #making sure we are not repeating any sequence in seqs[i][j][k]
                        if p1==lcs_max:
                            #print("seqs[i-1][j][k]", i-1, j, k, seqs[i2-1][j%2][k%2])
                            for l in seqs2[j2][k]:
                                tl = tuple(l)
                                if tl not in set_seqs:
                                    #set_seqs[tl] = 1
                                    set_seqs.add(tl)
                                    seqs[j][k].append(l)
                        if p2==lcs_max:
                            #print("seqs[i][j-1][k]", i, j-1, k, seqs[i2][j%2-1][k%2])
                            for l in seqs[j-1][k]:
                                tl = tuple(l)
                                if tl not in set_seqs:
                                    #set_seqs[tl] = 1
                                    set_seqs.add(tl)
                                    seqs[j][k].append(l)
                        if p3==lcs_max:
                            #print("seqs[i][j][k-1]", i, j, k-1, seqs[i2][j%2][k%2-1])
                            for l in seqs[j][k-1]:
                                tl = tuple(l)
                                if tl not in set_seqs:
                                    #set_seqs[tl] = 1
                                    set_seqs.add(tl)
                                    seqs[j][k].append(l)
                        if p4==lcs_max:
                            #print("seqs[i][j-1][k-1]", i, j-1, k-1, seqs[i2][j%2-1][k%2-1])
                            for l in seqs[j-1][k-1]:
                                tl = tuple(l)
                                if tl not in set_seqs:
                                    #set_seqs[tl] = 1
                                    set_seqs.add(tl)
                                    seqs[j][k].append(l)
                        if p5==lcs_max:
                            #print("seqs[i-1][j][k-1]", i-1, j, k-1, seqs[i2-1][j%2][k%2-1])
                            for l in seqs2[j2][k-1]:
                                tl = tuple(l)
                                if tl not in set_seqs:
                                    #set_seqs[tl] = 1
                                    set_seqs.add(tl)
                                    seqs[j][k].append(l)
                        if p6==lcs_max:
                            #print("seqs[i-1][j-1][k]", i-1, j-1, k, seqs[i2-1][j%2-1][k%2])
                            for l in seqs2[j2-1][k]:
                                tl = tuple(l)
                                if tl not in set_seqs:
                                    #set_seqs[tl] = 1
                                    set_seqs.add(tl)
                                    seqs[j][k].append(l)
                        #print("seqs[i][j][k]", i, j, k, seqs[i2][j%2][k%2])
                        set_seqs.clear() #clearing set for next iteration
                    #print("lcs_max",lcs_max, "p1-6", p1, p2, p3, p4, p5, p6)
                    len_lcs[i][j].append(lcs_max)
    #print("printing lcs")
    #a_max2 = a_max%2
    for l in seqs[b_max][c_max]:
        #print("lcs= ", l)
        pass
    return len_lcs[a_max][b_max][c_max]


#what i've learnt
#tuples take up much more space
#converting list to tuple does not take much time
#so, going back to using list, and also using set instead of dictionary
def lcs3_still_too_slow(a1, b1, c1): #also prints each lcs
    a1_max = len(a1)
    b1_max = len(b1)
    c1_max = len(c1)
    #a_max,a = sorted(
    if a1_max >= b1_max: #a is larger
        if a1_max >= c1_max: #a is largest
            a_max = a1_max
            b_max = b1_max
            c_max = c1_max
            a = a1
            b = b1
            c = c1
        else: #c is largest
            a_max = c1_max
            b_max = b1_max
            c_max = a1_max
            a = c1
            b = b1
            c = a1
    else: #b is larger
        if b1_max >= c1_max: #b is largest
            a_max = b1_max
            b_max = a1_max
            c_max = c1_max
            a = b1
            b = a1
            c = c1
        else: #c is largest
            a_max = c1_max
            b_max = b1_max
            c_max = a1_max
            a = c1
            b = b1
            c = a1
    #by the end of this, i've made sure "a" is the largest sequence. This minimizes the memory needed to store seqs

    len_lcs = []
    seqs = [] #list of actual lcs, now storing only 2 levels deep
    set_seqs = set() #making sure we are not repeating any sequence in seqs[i][j][k]
    for i in range(2): #creating elements ahead of time
        seqs.append([]) #for each i, create 2nd list
        for j in range(b_max + 1):
            seqs[i].append([]) #for each j, create 3rd list
            for k in range(c_max + 1):
                seqs[i][j].append([]) #for each k, creating 4th list

    for i in range(a_max + 1):
        len_lcs.append([]) #for each i, create 2nd list
        for j in range(b_max + 1):
            len_lcs[i].append([]) #for each j, create 3rd list
            for k in range(c_max + 1):
                #print("i,j,k", i, j, k)
                i2 = i%2
                if (i == 0) or (j==0) or (k==0):
                    len_lcs[i][j].append(0) #setting all boundary points to null. "n" denotes null
                    #seqs[i2][j][k] = [()] #setting all boundary points to list containing empty tuple
                    seqs[i2][j][k] = [[]] #setting all boundary points to list containing empty list
                else: #it means none of the indices are 0, so we are dealing with inside points
                    if (a[i-1]==b[j-1]) and (a[i-1]==c[k-1]): #using -1 since a,b,c are zero based
                        lcs_max = len_lcs[i-1][j-1][k-1] + 1 #since last element in each sequence matches, the len_lcs is 1 + len_lcs of the slightly smaller subsequences
                        seqs[i2][j][k] = [] #reset seqs for current indices
                        for l in seqs[i2-1][j-1][k-1]: #now add the lcs values from smaller subsequences, appending this element to each
                            #ltemp = l[:]
                            #ltemp.append(a[i-1])
                            ltemp = l + [a[i-1]]
                            seqs[i2][j][k].append(ltemp)
                            #print("l, ltemp",l, ltemp)
                        #print("seqs[i][j][k]", i, j, k, seqs[i2][j%2][k%2])
                    else:
                        p1 = len_lcs[i-1][j][k]
                        p2 = len_lcs[i][j-1][k]
                        p3 = len_lcs[i][j][k-1]
                        p4 = len_lcs[i][j-1][k-1]
                        p5 = len_lcs[i-1][j][k-1]
                        p6 = len_lcs[i-1][j-1][k]
                        lcs_max = max(p1, p2, p3, p4, p5, p6)
                        seqs[i2][j][k] = [] #reset seqs for current indices
                        #set_seqs = set() #making sure we are not repeating any sequence in seqs[i][j][k]
                        if p1==lcs_max:
                            #print("seqs[i-1][j][k]", i-1, j, k, seqs[i2-1][j%2][k%2])
                            for l in seqs[i2-1][j][k]:
                                tl = tuple(l)
                                if tl not in set_seqs:
                                    #set_seqs[tl] = 1
                                    set_seqs.add(tl)
                                    seqs[i2][j][k].append(l)
                        if p2==lcs_max:
                            #print("seqs[i][j-1][k]", i, j-1, k, seqs[i2][j%2-1][k%2])
                            for l in seqs[i2][j-1][k]:
                                tl = tuple(l)
                                if tl not in set_seqs:
                                    #set_seqs[tl] = 1
                                    set_seqs.add(tl)
                                    seqs[i2][j][k].append(l)
                        if p3==lcs_max:
                            #print("seqs[i][j][k-1]", i, j, k-1, seqs[i2][j%2][k%2-1])
                            for l in seqs[i2][j][k-1]:
                                tl = tuple(l)
                                if tl not in set_seqs:
                                    #set_seqs[tl] = 1
                                    set_seqs.add(tl)
                                    seqs[i2][j][k].append(l)
                        if p4==lcs_max:
                            #print("seqs[i][j-1][k-1]", i, j-1, k-1, seqs[i2][j%2-1][k%2-1])
                            for l in seqs[i2][j-1][k-1]:
                                tl = tuple(l)
                                if tl not in set_seqs:
                                    #set_seqs[tl] = 1
                                    set_seqs.add(tl)
                                    seqs[i2][j][k].append(l)
                        if p5==lcs_max:
                            #print("seqs[i-1][j][k-1]", i-1, j, k-1, seqs[i2-1][j%2][k%2-1])
                            for l in seqs[i2-1][j][k-1]:
                                tl = tuple(l)
                                if tl not in set_seqs:
                                    #set_seqs[tl] = 1
                                    set_seqs.add(tl)
                                    seqs[i2][j][k].append(l)
                        if p6==lcs_max:
                            #print("seqs[i-1][j-1][k]", i-1, j-1, k, seqs[i2-1][j%2-1][k%2])
                            for l in seqs[i2-1][j-1][k]:
                                tl = tuple(l)
                                if tl not in set_seqs:
                                    #set_seqs[tl] = 1
                                    set_seqs.add(tl)
                                    seqs[i2][j][k].append(l)
                        #print("seqs[i][j][k]", i, j, k, seqs[i2][j%2][k%2])
                        set_seqs.clear() #clearing set for next iteration
                    #print("lcs_max",lcs_max, "p1-6", p1, p2, p3, p4, p5, p6)
                    len_lcs[i][j].append(lcs_max)
    #print("printing lcs")
    a_max2 = a_max%2
    for l in seqs[a_max2][b_max][c_max]:
        #print("lcs= ", l)
        pass
    return len_lcs[a_max][b_max][c_max]

def lcs3_still_too_much_mem_and_time(a1, b1, c1): #also prints each lcs
    a1_max = len(a1)
    b1_max = len(b1)
    c1_max = len(c1)
    if a1_max >= b1_max: #a is larger
        if a1_max >= c1_max: #a is largest
            a_max = a1_max
            b_max = b1_max
            c_max = c1_max
            a = a1
            b = b1
            c = c1
        else: #c is largest
            a_max = c1_max
            b_max = b1_max
            c_max = a1_max
            a = c1
            b = b1
            c = a1
    else: #b is larger
        if b1_max >= c1_max: #b is largest
            a_max = b1_max
            b_max = a1_max
            c_max = c1_max
            a = b1
            b = a1
            c = c1
        else: #c is largest
            a_max = c1_max
            b_max = b1_max
            c_max = a1_max
            a = c1
            b = b1
            c = a1
    #by the end of this, i've made sure "a" is the largest sequence. This minimizes the memory needed to store seqs

    len_lcs = []
    seqs = [] #list of actual lcs, now storing only 2 levels deep
    for i in range(min(a_max+1, 2)): #creating elements ahead of time
        seqs.append([]) #for each i, create 2nd list
        for j in range(b_max + 1):
            seqs[i].append([]) #for each j, create 3rd list
            for k in range(c_max + 1):
                seqs[i][j].append([]) #for each k, creating 4th list

    for i in range(a_max + 1):
        len_lcs.append([]) #for each i, create 2nd list
        for j in range(b_max + 1):
            len_lcs[i].append([]) #for each j, create 3rd list
            for k in range(c_max + 1):
                #print("i,j,k", i, j, k)
                if (i == 0) or (j==0) or (k==0):
                    len_lcs[i][j].append(0) #setting all boundary points to null. "n" denotes null
                    seqs[i%2][j][k] = [[]] #setting all boundary points to list containing empty list
                else: #it means none of the indices are 0, so we are dealing with inside points
                    if (a[i-1]==b[j-1]) and (a[i-1]==c[k-1]): #since a,b,c are zero based
                        lcs_max = len_lcs[i-1][j-1][k-1] + 1 #if last element in each sequence matches, the len_lcs is 1 + len_lcs of the slightly smaller subsequences
                        seqs[i%2][j][k] = [] #reset seqs for current indices
                        for l in seqs[i%2-1][j-1][k-1]: #now add the lcs values from smaller subsequences, appending this element to each
                            ltemp = l[:]
                            ltemp.append(a[i-1])
                            seqs[i%2][j][k].append(ltemp)
                            #print("l, ltemp",l, ltemp)
                        #print("seqs[i][j][k]", i, j, k, seqs[i%2][j%2][k%2])
                    else:
                        p1 = len_lcs[i-1][j][k]
                        p2 = len_lcs[i][j-1][k]
                        p3 = len_lcs[i][j][k-1]
                        p4 = len_lcs[i][j-1][k-1]
                        p5 = len_lcs[i-1][j][k-1]
                        p6 = len_lcs[i-1][j-1][k]
                        lcs_max = max(p1, p2, p3, p4, p5, p6)
                        seqs[i%2][j][k] = [] #reset seqs for current indices
                        set_seqs = {} #making sure we are not repeating any sequence in seqs[i][j][k]
                        if p1==lcs_max:
                            #print("seqs[i-1][j][k]", i-1, j, k, seqs[i%2-1][j%2][k%2])
                            for l in seqs[i%2-1][j][k]:
                                tl = tuple(l)
                                if tl not in set_seqs:
                                    set_seqs[tl] = 1
                                    seqs[i%2][j][k].append(l)
                        if p2==lcs_max:
                            #print("seqs[i][j-1][k]", i, j-1, k, seqs[i%2][j%2-1][k%2])
                            for l in seqs[i%2][j-1][k]:
                                tl = tuple(l)
                                if tl not in set_seqs:
                                    set_seqs[tl] = 1
                                    seqs[i%2][j][k].append(l)
                        if p3==lcs_max:
                            #print("seqs[i][j][k-1]", i, j, k-1, seqs[i%2][j%2][k%2-1])
                            for l in seqs[i%2][j][k-1]:
                                tl = tuple(l)
                                if tl not in set_seqs:
                                    set_seqs[tl] = 1
                                    seqs[i%2][j][k].append(l)
                        if p4==lcs_max:
                            #print("seqs[i][j-1][k-1]", i, j-1, k-1, seqs[i%2][j%2-1][k%2-1])
                            for l in seqs[i%2][j-1][k-1]:
                                tl = tuple(l)
                                if tl not in set_seqs:
                                    set_seqs[tl] = 1
                                    seqs[i%2][j][k].append(l)
                        if p5==lcs_max:
                            #print("seqs[i-1][j][k-1]", i-1, j, k-1, seqs[i%2-1][j%2][k%2-1])
                            for l in seqs[i%2-1][j][k-1]:
                                tl = tuple(l)
                                if tl not in set_seqs:
                                    set_seqs[tl] = 1
                                    seqs[i%2][j][k].append(l)
                        if p6==lcs_max:
                            #print("seqs[i-1][j-1][k]", i-1, j-1, k, seqs[i%2-1][j%2-1][k%2])
                            for l in seqs[i%2-1][j-1][k]:
                                tl = tuple(l)
                                if tl not in set_seqs:
                                    set_seqs[tl] = 1
                                    seqs[i%2][j][k].append(l)
                        #print("seqs[i][j][k]", i, j, k, seqs[i%2][j%2][k%2])
                    #print("lcs_max",lcs_max, "p1-6", p1, p2, p3, p4, p5, p6)
                    len_lcs[i][j].append(lcs_max)
    #print("printing lcs")
    for l in seqs[a_max%2][b_max][c_max]:
        #print("lcs= ", l)
        pass
    return len_lcs[a_max][b_max][c_max]

#lowered memory requirement
def lcs3_notworking(a, b, c): #also prints each lcs
    a_max = len(a)
    b_max = len(b)
    c_max = len(c)
    len_lcs = []
    seqs = [] #list of actual lcs, now storing only 2 levels deep
    seqs2 = {}
    for i in range(min(a_max, 2)):
        seqs.append([]) #for each i, create 2nd list
        for j in range(min(b_max, 2)):
            seqs[i].append([]) #for each j, create 3rd list
            for k in range(min(c_max, 2)):
                seqs[i][j].append([]) #for each k, creating 4th list
    dirs = [] #stores the last direction '-' = right, '|' = down, '\' = diagonal
    for i in range(a_max + 1):
        len_lcs.append([]) #for each i, create 2nd list
        for j in range(b_max + 1):
            len_lcs[i].append([]) #for each j, create 3rd list
            for k in range(c_max + 1):
                #print("i,j,k", i, j, k)
                if (i == 0) or (j==0) or (k==0):
                    len_lcs[i][j].append(0) #setting all boundary points to null. "n" denotes null
                    #seqs[i][j].append([[]]) #setting all boundary points to list containing empty list
                    seqs[i%2][j%2][k%2] = [[]] #setting all boundary points to list containing empty list
                else: #it means none of the indices are 0, so we are dealing with inside points
                    if (a[i-1]==b[j-1]) and (a[i-1]==c[k-1]): #since a,b,c are zero based
                        #lcs_max = lcs3(a, b, c, a_max-1, b_max-1, c_max-1) + 1
                        lcs_max = len_lcs[i-1][j-1][k-1] + 1
                        #for each list in seqs[i-1][j-1][k-1], append a[i-1]
                        #set_seqs = {}
                        #seqs[i][j].append([]) #for each k, creating 4th list
                        #print("seqs[i-1][j-1][k-1]", i-1, j-1, k-1, seqs[i%2-1][j%2-1][k%2-1]), a[i-1]
                        seqs[i%2][j%2][k%2] = [] #reset seqs for current indices
                        for l in seqs[i%2-1][j%2-1][k%2-1]:
                            ltemp = l[:]
                            ltemp.append(a[i-1])
                            #set_seqs[tuple(ltemp)] = 1
                            seqs[i%2][j%2][k%2].append(ltemp)
                            #print("l, ltemp",l, ltemp)
                        #print("seqs[i][j][k]", i, j, k, seqs[i%2][j%2][k%2])
                    else:
                        p1 = len_lcs[i-1][j][k]
                        p2 = len_lcs[i][j-1][k]
                        p3 = len_lcs[i][j][k-1]
                        p4 = len_lcs[i][j-1][k-1]
                        p5 = len_lcs[i-1][j][k-1]
                        p6 = len_lcs[i-1][j-1][k]
                        lcs_max = max(p1, p2, p3, p4, p5, p6)
                        #seqs[i][j].append([]) #for each k, creating 4th list
                        seqs[i%2][j%2][k%2] = [] #reset seqs for current indices
                        set_seqs = {} #making sure we are not repeating any sequence in seqs[i][j][k]
                        if p1==lcs_max:
                            #print("seqs[i-1][j][k]", i-1, j, k, seqs[i%2-1][j%2][k%2])
                            if (j==1) or (k==1):
                                if i == 1:
                                    seqtemp = [[]]
                                else:
                                    seqtemp = seqs2[(i-1, j, k)]
                            for l in seqtemp:
                                tl = tuple(l)
                                if tl not in set_seqs:
                                    set_seqs[tl] = 1
                                    seqs[i%2][j%2][k%2].append(l)
                        if p2==lcs_max:
                            #print("seqs[i][j-1][k]", i, j-1, k, seqs[i%2][j%2-1][k%2])
                            if (j-1==1) or (k==1):
                                if j==1:
                                    seqtemp = [[]]
                                else:
                                    seqtemp = seqs2[(i, j-1, k)]
                            for l in seqtemp:
                                tl = tuple(l)
                                if tl not in set_seqs:
                                    set_seqs[tl] = 1
                                    seqs[i%2][j%2][k%2].append(l)
                        if p3==lcs_max:
                            #print("seqs[i][j][k-1]", i, j, k-1, seqs[i%2][j%2][k%2-1])
                            if (j==1) or (k-1==1):
                                if k==1:
                                    seqtemp = [[]]
                                else:
                                    seqtemp = seqs2[i, j, k-1]
                            for l in seqtemp:
                                tl = tuple(l)
                                if tl not in set_seqs:
                                    set_seqs[tl] = 1
                                    seqs[i%2][j%2][k%2].append(l)
                        if p4==lcs_max:
                            #print("seqs[i][j-1][k-1]", i, j-1, k-1, seqs[i%2][j%2-1][k%2-1])
                            if (j-1==1) or (k-1==1):
                                if j==1 or k==1:
                                    seqtemp = [[]]
                                else:
                                    seqtemp = seqs2[i, j-1, k-1]
                            for l in seqtemp:
                                tl = tuple(l)
                                if tl not in set_seqs:
                                    set_seqs[tl] = 1
                                    seqs[i%2][j%2][k%2].append(l)
                        if p5==lcs_max:
                            #print("seqs[i-1][j][k-1]", i-1, j, k-1, seqs[i%2-1][j%2][k%2-1])
                            if (j==1) or (k-1==1):
                                if i==1 or k==1:
                                    seqtemp = [[]]
                                else:
                                    seqtemp = seqs2[(i-1, j, k-1)]
                            for l in seqtemp:
                                tl = tuple(l)
                                if tl not in set_seqs:
                                    set_seqs[tl] = 1
                                    seqs[i%2][j%2][k%2].append(l)
                        if p6==lcs_max:
                            #print("seqs[i-1][j-1][k]", i-1, j-1, k, seqs[i%2-1][j%2-1][k%2])
                            if (j-1==1) or (k==1):
                                if i==1 or j==1:
                                    seqtemp = [[]]
                                else:
                                    seqtemp = seqs2[(i-1, j-1, k)]
                            for l in seqtemp:
                                tl = tuple(l)
                                if tl not in set_seqs:
                                    set_seqs[tl] = 1
                                    seqs[i%2][j%2][k%2].append(l)
                        #print("seqs[i][j][k]", i, j, k, seqs[i%2][j%2][k%2])
                    #print("lcs_max",lcs_max, "p1-6", p1, p2, p3, p4, p5, p6)
                    len_lcs[i][j].append(lcs_max)
                    if (i==1) or (j==1) or (k==1): #preserving initial values, will need when i traverse back to initial k (for each new j) or initial j (for each new i)
                        seqs2[(i,j,k)] = seqs[i%2][j%2][k%2]
    print("printing lcs")
    for l in seqs[a_max%2][b_max%2][c_max%2]:
        print("lcs= ", l)
        pass
    return len_lcs[a_max][b_max][c_max]


#lowered memory requirement
def lcs3_incorrect_travel(a, b, c): #also prints each lcs
    a_max = len(a)
    b_max = len(b)
    c_max = len(c)
    len_lcs = []
    seqs = [] #list of actual lcs, now storing only 2 levels deep
    for i in range(min(a_max, 2)):
        seqs.append([]) #for each i, create 2nd list
        for j in range(min(b_max, 2)):
            seqs[i].append([]) #for each j, create 3rd list
            for k in range(min(c_max, 2)):
                seqs[i][j].append([]) #for each k, creating 4th list
    dirs = [] #stores the last direction '-' = right, '|' = down, '\' = diagonal
    for i in range(a_max + 1):
        len_lcs.append([]) #for each i, create 2nd list
        for j in range(b_max + 1):
            len_lcs[i].append([]) #for each j, create 3rd list
            for k in range(c_max + 1):
                print("i,j,k", i, j, k)
                if (i == 0) or (j==0) or (k==0):
                    len_lcs[i][j].append(0) #setting all boundary points to null. "n" denotes null
                    #seqs[i][j].append([[]]) #setting all boundary points to list containing empty list
                    seqs[i%2][j%2][k%2] = [[]] #setting all boundary points to list containing empty list
                else: #it means none of the indices are 0, so we are dealing with inside points
                    if (a[i-1]==b[j-1]) and (a[i-1]==c[k-1]): #since a,b,c are zero based
                        #lcs_max = lcs3(a, b, c, a_max-1, b_max-1, c_max-1) + 1
                        lcs_max = len_lcs[i-1][j-1][k-1] + 1
                        #for each list in seqs[i-1][j-1][k-1], append a[i-1]
                        #set_seqs = {}
                        #seqs[i][j].append([]) #for each k, creating 4th list
                        print("seqs[i-1][j-1][k-1]", i-1, j-1, k-1, seqs[i%2-1][j%2-1][k%2-1]), a[i-1]
                        seqs[i%2][j%2][k%2] = [] #reset seqs for current indices
                        for l in seqs[i%2-1][j%2-1][k%2-1]:
                            ltemp = l[:]
                            ltemp.append(a[i-1])
                            #set_seqs[tuple(ltemp)] = 1
                            seqs[i%2][j%2][k%2].append(ltemp)
                            print("l, ltemp",l, ltemp)
                        print("seqs[i][j][k]", i, j, k, seqs[i%2][j%2][k%2])
                    else:
                        p1 = len_lcs[i-1][j][k]
                        p2 = len_lcs[i][j-1][k]
                        p3 = len_lcs[i][j][k-1]
                        p4 = len_lcs[i][j-1][k-1]
                        p5 = len_lcs[i-1][j][k-1]
                        p6 = len_lcs[i-1][j-1][k]
                        lcs_max = max(p1, p2, p3, p4, p5, p6)
                        #seqs[i][j].append([]) #for each k, creating 4th list
                        seqs[i%2][j%2][k%2] = [] #reset seqs for current indices
                        set_seqs = {} #making sure we are not repeating any sequence in seqs[i][j][k]
                        if p1==lcs_max:
                            print("seqs[i-1][j][k]", i-1, j, k, seqs[i%2-1][j%2][k%2])
                            for l in seqs[i%2-1][j%2][k%2]:
                                tl = tuple(l)
                                if tl not in set_seqs:
                                    set_seqs[tl] = 1
                                    seqs[i%2][j%2][k%2].append(l)
                        if p2==lcs_max:
                            print("seqs[i][j-1][k]", i, j-1, k, seqs[i%2][j%2-1][k%2])
                            for l in seqs[i%2][j%2-1][k%2]:
                                tl = tuple(l)
                                if tl not in set_seqs:
                                    set_seqs[tl] = 1
                                    seqs[i%2][j%2][k%2].append(l)
                        if p3==lcs_max:
                            print("seqs[i][j][k-1]", i, j, k-1, seqs[i%2][j%2][k%2-1])
                            for l in seqs[i%2][j%2][k%2-1]:
                                tl = tuple(l)
                                if tl not in set_seqs:
                                    set_seqs[tl] = 1
                                    seqs[i%2][j%2][k%2].append(l)
                        if p4==lcs_max:
                            print("seqs[i][j-1][k-1]", i, j-1, k-1, seqs[i%2][j%2-1][k%2-1])
                            for l in seqs[i%2][j%2-1][k%2-1]:
                                tl = tuple(l)
                                if tl not in set_seqs:
                                    set_seqs[tl] = 1
                                    seqs[i%2][j%2][k%2].append(l)
                        if p5==lcs_max:
                            print("seqs[i-1][j][k-1]", i-1, j, k-1, seqs[i%2-1][j%2][k%2-1])
                            for l in seqs[i%2-1][j%2][k%2-1]:
                                tl = tuple(l)
                                if tl not in set_seqs:
                                    set_seqs[tl] = 1
                                    seqs[i%2][j%2][k%2].append(l)
                        if p6==lcs_max:
                            print("seqs[i-1][j-1][k]", i-1, j-1, k, seqs[i%2-1][j%2-1][k%2])
                            for l in seqs[i%2-1][j%2-1][k%2]:
                                tl = tuple(l)
                                if tl not in set_seqs:
                                    set_seqs[tl] = 1
                                    seqs[i%2][j%2][k%2].append(l)
                        print("seqs[i][j][k]", i, j, k, seqs[i%2][j%2][k%2])
                    #print("lcs_max",lcs_max, "p1-6", p1, p2, p3, p4, p5, p6)
                    len_lcs[i][j].append(lcs_max)
    print("printing lcs")
    for l in seqs[a_max%2][b_max%2][c_max%2]:
        print("lcs= ", l)
        pass
    return len_lcs[a_max][b_max][c_max]

def lcs3_high_mem(a, b, c): #also prints each lcs
    a_max = len(a)
    b_max = len(b)
    c_max = len(c)
    len_lcs = []
    seqs = [] #list of actual lcs
    dirs = [] #stores the last direction '-' = right, '|' = down, '\' = diagonal
    for i in range(a_max + 1):
        len_lcs.append([]) #for each i, create 2nd list
        seqs.append([]) #for each i, create 2nd list
        for j in range(b_max + 1):
            len_lcs[i].append([]) #for each j, create 3rd list
            seqs[i].append([]) #for each j, create 3rd list
            for k in range(c_max + 1):
                print("i,j,k", i, j, k)
                if (i == 0) or (j==0) or (k==0):
                    len_lcs[i][j].append(0) #setting all boundary points to null. "n" denotes null
                    seqs[i][j].append([[]]) #setting all boundary points to list containing empty list
                else: #it means none of the indices are 0, so we are dealing with inside points
                    if (a[i-1]==b[j-1]) and (a[i-1]==c[k-1]): #since a,b,c are zero based
                        #lcs_max = lcs3(a, b, c, a_max-1, b_max-1, c_max-1) + 1
                        lcs_max = len_lcs[i-1][j-1][k-1] + 1
                        #for each list in seqs[i-1][j-1][k-1], append a[i-1]
                        #set_seqs = {}
                        seqs[i][j].append([]) #for each k, creating 4th list
                        print("seqs[i-1][j-1][k-1]", i-1, j-1, k-1, seqs[i-1][j-1][k-1])
                        for l in seqs[i-1][j-1][k-1]:
                            ltemp = l[:]
                            ltemp.append(a[i-1])
                            #set_seqs[tuple(ltemp)] = 1
                            seqs[i][j][k].append(ltemp)
                            print("l, ltemp",l, ltemp)
                        print("seqs[i][j][k]", i, j, k, seqs[i][j][k])
                    else:
                        p1 = len_lcs[i-1][j][k]
                        p2 = len_lcs[i][j-1][k]
                        p3 = len_lcs[i][j][k-1]
                        p4 = len_lcs[i][j-1][k-1]
                        p5 = len_lcs[i-1][j][k-1]
                        p6 = len_lcs[i-1][j-1][k]
                        lcs_max = max(p1, p2, p3, p4, p5, p6)
                        seqs[i][j].append([]) #for each k, creating 4th list
                        set_seqs = {} #making sure we are not repeating any sequence in seqs[i][j][k]
                        if p1==lcs_max:
                            print("seqs[i-1][j][k]", i-1, j, k, seqs[i-1][j][k])
                            for l in seqs[i-1][j][k]:
                                tl = tuple(l)
                                if tl not in set_seqs:
                                    set_seqs[tl] = 1
                                    seqs[i][j][k].append(l)
                        if p2==lcs_max:
                            print("seqs[i][j-1][k]", i, j-1, k, seqs[i][j-1][k])
                            for l in seqs[i][j-1][k]:
                                tl = tuple(l)
                                if tl not in set_seqs:
                                    set_seqs[tl] = 1
                                    seqs[i][j][k].append(l)
                        if p3==lcs_max:
                            print("seqs[i][j][k-1]", i, j, k-1, seqs[i][j][k-1])
                            for l in seqs[i][j][k-1]:
                                tl = tuple(l)
                                if tl not in set_seqs:
                                    set_seqs[tl] = 1
                                    seqs[i][j][k].append(l)
                        if p4==lcs_max:
                            print("seqs[i][j-1][k-1]", i, j-1, k-1, seqs[i][j-1][k-1])
                            for l in seqs[i][j-1][k-1]:
                                tl = tuple(l)
                                if tl not in set_seqs:
                                    set_seqs[tl] = 1
                                    seqs[i][j][k].append(l)
                        if p5==lcs_max:
                            print("seqs[i-1][j][k-1]", i-1, j, k-1, seqs[i-1][j][k-1])
                            for l in seqs[i-1][j][k-1]:
                                tl = tuple(l)
                                if tl not in set_seqs:
                                    set_seqs[tl] = 1
                                    seqs[i][j][k].append(l)
                        if p6==lcs_max:
                            print("seqs[i-1][j-1][k]", i-1, j-1, k, seqs[i-1][j-1][k])
                            for l in seqs[i-1][j-1][k]:
                                tl = tuple(l)
                                if tl not in set_seqs:
                                    set_seqs[tl] = 1
                                    seqs[i][j][k].append(l)
                        print("seqs[i][j][k]", i, j, k, seqs[i][j][k])
                    #print("lcs_max",lcs_max, "p1-6", p1, p2, p3, p4, p5, p6)
                    len_lcs[i][j].append(lcs_max)
    #print("printing lcs")
    for l in seqs[a_max][b_max][c_max]:
        print("lcs= ", l)
        pass
    return len_lcs[a_max][b_max][c_max]

#light version, does not show actual sequences
def lcs3_light(a, b, c):
    a_max = len(a)
    b_max = len(b)
    c_max = len(c)
    lcs = []
    dirs = [] #stores the last direction '-' = right, '|' = down, '\' = diagonal
    for i in range(a_max + 1):
        lcs.append([]) #for each i, create 2nd list
        for j in range(b_max + 1):
            lcs[i].append([]) #for each j, create 3rd list
            for k in range(c_max + 1):
                #print("i,j,k", i, j, k)
                if (i == 0) or (j==0) or (k==0):
                    lcs[i][j].append(0) #setting all boundary points to null. "n" denotes null
                else: #it means none of the indices are 0, so we are dealing with inside points
                    if (a[i-1]==b[j-1]) and (a[i-1]==c[k-1]): #since a,b,c are zero based
                        #lcs_max = lcs3(a, b, c, a_max-1, b_max-1, c_max-1) + 1
                        lcs_max = lcs[i-1][j-1][k-1] + 1
                    else:
                        p1 = lcs[i-1][j][k]
                        p2 = lcs[i][j-1][k]
                        p3 = lcs[i][j][k-1]
                        p4 = lcs[i][j-1][k-1]
                        p5 = lcs[i-1][j][k-1]
                        p6 = lcs[i-1][j-1][k]
                        lcs_max = max(p1, p2, p3, p4, p5, p6)
                    #print("lcs_max",lcs_max, "p1-6", p1, p2, p3, p4, p5, p6)
                    lcs[i][j].append(lcs_max)
    return lcs[a_max][b_max][c_max]

def edit_distance3(s, t):
    #write your code here
    m = len(s)
    n = len(t)
    edit_dist = []
    ops = [] #stores last operation 'r' = right, 'w' = down, 'd' = diagonal, to get to this point in the 2-d matrix
    num_paths = 1 #stores the number of possible paths to minimum edit distance
    #for i in range(m):
    #    edit_dist.append([i]) #filling the 0th column
    for i in range(m+1):
        edit_dist.append([i]) #filling the 0th column
        if i > 0:
            ops.append(['d'])
        else:
            ops.append(['n']) #not valid op on the top-left corner of matrix!
        for j in range(1,n+1):
            if i > 0:
                right = edit_dist[i][j-1] + 1, 'r'
                down = edit_dist[i-1][j] + 1, 'w'
                if (s[i-1] == t[j-1]):
                    diag = edit_dist[i-1][j-1], 'd'
                else:
                    diag = edit_dist[i-1][j-1] + 1, 'd'
                ed = min(right, down, diag)
                edit_dist[i].append(ed[0])
                #now see if more than one option matched min
                dir = ""
                if (ed[0] == right[0]):
                    dir += "r"
                if (ed[0] == down[0]):
                    dir += "w"
                if (ed[0] == diag[0]):
                    dir += "d"
                ops[i].append(dir)
            else:
                edit_dist[i].append(j) #0th row
                ops[i].append('r')
    #at this point, i = m and j = n
    #now let's reconstruct the sequence of matches
    for k in range(m+1):
        for l in range(n+1):
            print(edit_dist[k][l],ops[k][l], end=" ", sep="")
        print()
    print("i, j", i, j)
    #i need to create segments of paths, each segment covering divergent point to convergent point.
    forks = []
    dic_forks = {} #key is divergence point, value is list of
    #dic_points
    #while (i >= 0) and (j >= 0):
    paths = {}
    paths_left = True
    while paths_left:
        paths_left = False
        matches = [] #this will store list of matching chars
        i = m
        j = n
        while (i > 0) and (j > 0):
            opm = ops[i][j]
            #print("opm", opm)
            #now this might be more than one direction!
            #so, how do i ensure i traverse each possible path?
            #i'll park each fork in a list?
            #while len(opm)>1:
            #    forks.append([i, j, opm[-1]], len(matches)) #storing the number of matches found so far
            #    if (i, j) not in dic_forks:
            #        dic_forks[(i,j)] = [len(matches)]
            #    else:
            #        dic_forks[(i,j)].append(len(matches))
            #    opm = opm[:-1] #truncating last element
            #now opm just contains last remaining dir
            op = opm[0]
            if len(opm) > 1:
                paths_left = True
                ops[i][j] = opm[1:]
            if op == 'd':
                i = i - 1
                j = j - 1
                #if (i >= 0) and (j >= 0) and (s[i] == t[j]):
                if (s[i] == t[j]):
                    print("i,j,s[i]", i,j,s[i])
                    matches.append(s[i])
            elif op == 'r':
                j = j - 1
            elif op == 'w':
                i = i - 1
            else:
                print("unexpected op", op)
        matches.reverse()
        paths[tuple(matches)] = matches #the value does not matter. i am just using the hash as a way of storing the set of keys

    #matches2 = reversed(matches)
    #print(edit_dist[m][n], matches2)
    matches_list = []
    for match in paths.keys():
        matches_list.append(paths[match])
    return edit_dist[m][n], matches_list


def edit_distance2(s, t):
    #write your code here
    m = len(s)
    n = len(t)
    edit_dist = []
    matches = [] #this will store list of matching chars
    ops = [] #stores last operation 'r' = right, 'w' = down, 'd' = diagonal, to get to this point in the 2-d matrix
    num_paths = 1 #stores the number of possible paths to minimum edit distance
    #for i in range(m):
    #    edit_dist.append([i]) #filling the 0th column
    for i in range(m+1):
        edit_dist.append([i]) #filling the 0th column
        if i > 0:
            ops.append(['d'])
        else:
            ops.append(['n']) #not valid op on the top-left corner of matrix!
        for j in range(1,n+1):
            if i > 0:
                right = edit_dist[i][j-1] + 1, 'r'
                down = edit_dist[i-1][j] + 1, 'w'
                if (s[i-1] == t[j-1]):
                    diag = edit_dist[i-1][j-1], 'd'
                else:
                    diag = edit_dist[i-1][j-1] + 1, 'd'
                ed = min(right, down, diag)
                edit_dist[i].append(ed[0])
                #now see if more than one option matched min
                dir = ""
                if (ed[0] == right[0]):
                    dir += "r"
                if (ed[0] == down[0]):
                    dir += "w"
                if (ed[0] == diag[0]):
                    dir += "d"
                ops[i].append(dir)
            else:
                edit_dist[i].append(j) #0th row
                ops[i].append('r')
    #at this point, i = m and j = n
    #now let's reconstruct the sequence of matches
    for k in range(m+1):
        for l in range(n+1):
            print(edit_dist[k][l],ops[k][l], end=" ", sep="")
        print()
    print("i, j", i, j)
    #i need to create segments of paths, each segment covering divergent point to convergent point.
    forks = []
    dic_forks = {} #key is divergence point, value is list of
    #dic_points
    #while (i >= 0) and (j >= 0):
    while (i > 0) and (j > 0):
        opm = ops[i][j]
        #print("opm", opm)
        #now this might be more than one direction!
        #so, how do i ensure i traverse each possible path?
        #i'll park each fork in a list?
        while len(opm)>1:
            forks.append([i, j, opm[-1]], len(matches)) #storing the number of matches found so far
            if (i, j) not in dic_forks:
                dic_forks[(i,j)] = [len(matches)]
            else:
                dic_forks[(i,j)].append(len(matches))
            opm = opm[:-1] #truncating last element
        #now opm just contains last remaining dir
        op = opm[0]
        if op == 'd':
            i = i - 1
            j = j - 1
            #if (i >= 0) and (j >= 0) and (s[i] == t[j]):
            if (s[i] == t[j]):
                print("i,j,s[i]", i,j,s[i])
                matches.append(s[i])
        elif op == 'r':
            j = j - 1
        elif op == 'w':
            i = i - 1
        else:
            print("unexpected op", op)
    #now we need to go thru this again, to find alternate paths

    #matches2 = reversed(matches)
    #print(edit_dist[m][n], matches2)
    matches.reverse()
    return edit_dist[m][n], matches







def lcs3_old(a, b, c):
    #write your code here
    e_d,matches = edit_distance2(a, b)
    print(matches)
    return min(len(a), len(b), len(c))

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))
    #print(lcs3_high_mem(a, b, c))
