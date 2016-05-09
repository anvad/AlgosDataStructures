#Uses python3

import sys

#using sets instead of lists
#@profile
def lcs3(a1, b1, c1): #also prints each lcs
    (c_max,c),(b_max,b),(a_max,a) = sorted([(len(a1),a1), (len(b1),b1), (len(c1),c1)])
    #print(a_max,a)
    #print(b_max,b)
    #print(c_max,c)
    #now, i've made sure "a" is the largest sequence. This minimizes the memory needed to store seqs

    len_lcs = []
    seqs = [] #list of actual lcs, now storing only 1 level deep
    seqs2 = [] #contains 2 row of sequences from diagonal line in lower level and for current line in lower level
    #set_seqs = set() #making sure we are not repeating any sequence in seqs[i][j][k]
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
                    #seqs[j][k] = [()] #setting all boundary points to list containing empty tuple
                    #seqs[j][k] = [[]] #setting all boundary points to list containing empty list
                    seqs[j][k] = set([()]) #setting all boundary points to list containing empty list
                else: #it means none of the indices are 0, so we are dealing with inside points
                    if (a[i-1]==b[j-1]) and (a[i-1]==c[k-1]): #using -1 since a,b,c are zero based
                        lcs_max = len_lcs[i-1][j-1][k-1] + 1 #since last element in each sequence matches, the len_lcs is 1 + len_lcs of the slightly smaller subsequences
                        #seqs[j][k] = [] #reset seqs for current indices
                        #for l in seqs2[j2-1][k-1]: #now add the lcs values from smaller subsequences, appending this element to each
                            #ltemp = l[:]
                            #ltemp.append(a[i-1])
                        #    ltemp = l + [a[i-1]]
                        #    seqs[j][k].append(ltemp)
                            #print("l, ltemp",l, ltemp)
                        #seqs[j][k] = [l + (a[i-1],) for l in seqs2[j2-1][k-1]]
                        #seqs[j][k] = [l + [a[i-1]] for l in seqs2[j2-1][k-1]]
                        seqs[j][k] = set([l + (a[i-1],) for l in seqs2[j2-1][k-1]])
                        #seqs[j][k] = seqs2[j2-1][k-1]
                        #for l in seqs[j][k]:
                        #    l.append(a[i-1])
                        #print("seqs[i][j][k]", i, j, k, seqs[i2][j%2][k%2])
                    else:
                        p1 = len_lcs[i-1][j][k]
                        p2 = len_lcs[i][j-1][k]
                        p3 = len_lcs[i][j][k-1]
                        p4 = len_lcs[i][j-1][k-1]
                        p5 = len_lcs[i-1][j][k-1]
                        p6 = len_lcs[i-1][j-1][k]
                        lcs_max = max(p1, p2, p3, p4, p5, p6)
                        #seqs[j][k] = [] #reset seqs for current indices
                        #set_seqs = set() #making sure we are not repeating any sequence in seqs[i][j][k]
                        seqs[j][k] = set()
                        if p1==lcs_max:
                            #print("seqs[i-1][j][k]", i-1, j, k, seqs[i2-1][j%2][k%2])
                            for l in seqs2[j2][k]:
                                seqs[j][k].add(l)
                        if p2==lcs_max:
                            #print("seqs[i][j-1][k]", i, j-1, k, seqs[i2][j%2-1][k%2])
                            for l in seqs[j-1][k]:
                                seqs[j][k].add(l)
                        if p3==lcs_max:
                            #print("seqs[i][j][k-1]", i, j, k-1, seqs[i2][j%2][k%2-1])
                            for l in seqs[j][k-1]:
                                seqs[j][k].add(l)
                        if p4==lcs_max:
                            #print("seqs[i][j-1][k-1]", i, j-1, k-1, seqs[i2][j%2-1][k%2-1])
                            for l in seqs[j-1][k-1]:
                                seqs[j][k].add(l)
                        if p5==lcs_max:
                            #print("seqs[i-1][j][k-1]", i-1, j, k-1, seqs[i2-1][j%2][k%2-1])
                            for l in seqs2[j2][k-1]:
                                seqs[j][k].add(l)
                        if p6==lcs_max:
                            #print("seqs[i-1][j-1][k]", i-1, j-1, k, seqs[i2-1][j%2-1][k%2])
                            for l in seqs2[j2-1][k]:
                                seqs[j][k].add(l)
                        #seqs[j][k] = list(set_seqs)
                        #print("seqs[i][j][k]", i, j, k, seqs[i2][j%2][k%2])
                        #set_seqs.clear() #clearing set for next iteration
                    #print("lcs_max",lcs_max, "p1-6", p1, p2, p3, p4, p5, p6)
                    len_lcs[i][j].append(lcs_max)
    print("num lcs", len(seqs[b_max][c_max]))
    #a_max2 = a_max%2
    for l in seqs[b_max][c_max]:
        print("lcs= ", l)
        pass
    return len_lcs[a_max][b_max][c_max]


#now i am finally inside memory limits!
#taking 20 secs though, whereas the limit is only 10
#so how to reduce compute time?
#tried not checking set before adding.. no diff to speed but more memory used
#tried using tuples, to avoid time spent in converting to tuple and back to list.. no diff to speed but exceeded memory limtits
def lcs3_slow(a1, b1, c1): #also prints each lcs
    (c_max,c),(b_max,b),(a_max,a) = sorted([(len(a1),a1), (len(b1),b1), (len(c1),c1)])
    #print(a_max,a)
    #print(b_max,b)
    #print(c_max,c)
    #now, i've made sure "a" is the largest sequence. This minimizes the memory needed to store seqs

    len_lcs = []
    seqs = [] #list of actual lcs, now storing only 1 level deep
    seqs2 = [] #contains 2 row of sequences from diagonal line in lower level and for current line in lower level
    #set_seqs = set() #making sure we are not repeating any sequence in seqs[i][j][k]
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
                    #seqs[j][k] = [()] #setting all boundary points to list containing empty tuple
                    seqs[j][k] = [[]] #setting all boundary points to list containing empty list
                else: #it means none of the indices are 0, so we are dealing with inside points
                    if (a[i-1]==b[j-1]) and (a[i-1]==c[k-1]): #using -1 since a,b,c are zero based
                        lcs_max = len_lcs[i-1][j-1][k-1] + 1 #since last element in each sequence matches, the len_lcs is 1 + len_lcs of the slightly smaller subsequences
                        #seqs[j][k] = [] #reset seqs for current indices
                        #for l in seqs2[j2-1][k-1]: #now add the lcs values from smaller subsequences, appending this element to each
                            #ltemp = l[:]
                            #ltemp.append(a[i-1])
                        #    ltemp = l + [a[i-1]]
                        #    seqs[j][k].append(ltemp)
                            #print("l, ltemp",l, ltemp)
                        #seqs[j][k] = [l + (a[i-1],) for l in seqs2[j2-1][k-1]]
                        seqs[j][k] = [l + [a[i-1]] for l in seqs2[j2-1][k-1]]
                        #seqs[j][k] = seqs2[j2-1][k-1]
                        #for l in seqs[j][k]:
                        #    l.append(a[i-1])
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
                        set_seqs = set() #making sure we are not repeating any sequence in seqs[i][j][k]
                        if p1==lcs_max:
                            #print("seqs[i-1][j][k]", i-1, j, k, seqs[i2-1][j%2][k%2])
                            for l in seqs2[j2][k]:
                                tl = tuple(l)
                                if tl not in set_seqs:
                                    set_seqs.add(tl)
                                    seqs[j][k].append(l)
                        if p2==lcs_max:
                            #print("seqs[i][j-1][k]", i, j-1, k, seqs[i2][j%2-1][k%2])
                            for l in seqs[j-1][k]:
                                tl = tuple(l)
                                if tl not in set_seqs:
                                    set_seqs.add(tl)
                                    seqs[j][k].append(l)
                        if p3==lcs_max:
                            #print("seqs[i][j][k-1]", i, j, k-1, seqs[i2][j%2][k%2-1])
                            for l in seqs[j][k-1]:
                                tl = tuple(l)
                                if tl not in set_seqs:
                                    set_seqs.add(tl)
                                    seqs[j][k].append(l)
                        if p4==lcs_max:
                            #print("seqs[i][j-1][k-1]", i, j-1, k-1, seqs[i2][j%2-1][k%2-1])
                            for l in seqs[j-1][k-1]:
                                tl = tuple(l)
                                if tl not in set_seqs:
                                    set_seqs.add(tl)
                                    seqs[j][k].append(l)
                        if p5==lcs_max:
                            #print("seqs[i-1][j][k-1]", i-1, j, k-1, seqs[i2-1][j%2][k%2-1])
                            for l in seqs2[j2][k-1]:
                                tl = tuple(l)
                                if tl not in set_seqs:
                                    set_seqs.add(tl)
                                    seqs[j][k].append(l)
                        if p6==lcs_max:
                            #print("seqs[i-1][j-1][k]", i-1, j-1, k, seqs[i2-1][j%2-1][k%2])
                            for l in seqs2[j2-1][k]:
                                tl = tuple(l)
                                if tl not in set_seqs:
                                    set_seqs.add(tl)
                                    seqs[j][k].append(l)
                        #seqs[j][k] = list(set_seqs)
                        #print("seqs[i][j][k]", i, j, k, seqs[i2][j%2][k%2])
                        #set_seqs.clear() #clearing set for next iteration
                    #print("lcs_max",lcs_max, "p1-6", p1, p2, p3, p4, p5, p6)
                    len_lcs[i][j].append(lcs_max)
    print("num lcs", len(seqs[b_max][c_max]))
    #a_max2 = a_max%2
    for l in seqs[b_max][c_max]:
        print("lcs= ", l)
        pass
    return len_lcs[a_max][b_max][c_max]

#so, not ensuring we store only unique entries, really quickly became a time and space problem!
def lcs3_really_slow_really_big(a1, b1, c1): #also prints each lcs
    (c_max,c),(b_max,b),(a_max,a) = sorted([(len(a1),a1), (len(b1),b1), (len(c1),c1)])
    #print(a_max,a)
    #print(b_max,b)
    #print(c_max,c)
    #now, i've made sure "a" is the largest sequence. This minimizes the memory needed to store seqs

    len_lcs = []
    seqs = [] #list of actual lcs, now storing only 1 level deep
    seqs2 = [] #contains 2 row of sequences from diagonal line in lower level and for current line in lower level
    #set_seqs = set() #making sure we are not repeating any sequence in seqs[i][j][k]
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
                                seqs[j][k].append(l)
                        if p2==lcs_max:
                            #print("seqs[i][j-1][k]", i, j-1, k, seqs[i2][j%2-1][k%2])
                            for l in seqs[j-1][k]:
                                seqs[j][k].append(l)
                        if p3==lcs_max:
                            #print("seqs[i][j][k-1]", i, j, k-1, seqs[i2][j%2][k%2-1])
                            for l in seqs[j][k-1]:
                                seqs[j][k].append(l)
                        if p4==lcs_max:
                            #print("seqs[i][j-1][k-1]", i, j-1, k-1, seqs[i2][j%2-1][k%2-1])
                            for l in seqs[j-1][k-1]:
                                seqs[j][k].append(l)
                        if p5==lcs_max:
                            #print("seqs[i-1][j][k-1]", i-1, j, k-1, seqs[i2-1][j%2][k%2-1])
                            for l in seqs2[j2][k-1]:
                                seqs[j][k].append(l)
                        if p6==lcs_max:
                            #print("seqs[i-1][j-1][k]", i-1, j-1, k, seqs[i2-1][j%2-1][k%2])
                            for l in seqs2[j2-1][k]:
                                seqs[j][k].append(l)
                        #print("seqs[i][j][k]", i, j, k, seqs[i2][j%2][k%2])
                        #set_seqs.clear() #clearing set for next iteration
                    #print("lcs_max",lcs_max, "p1-6", p1, p2, p3, p4, p5, p6)
                    len_lcs[i][j].append(lcs_max)
    #print("printing lcs")
    #a_max2 = a_max%2
    set_seqs = set()
    for l in seqs[b_max][c_max]:
        tl = tuple(l)
        set_seqs.add(tl)

    for l in set_seqs:
        #print("lcs=", l)
        pass
    return len_lcs[a_max][b_max][c_max]

#using union did not lower speed, but made memory usage even worse!
def lcs3_slow_bigger(a1, b1, c1): #also prints each lcs
    (c_max,c),(b_max,b),(a_max,a) = sorted([(len(a1),a1), (len(b1),b1), (len(c1),c1)])
    #print(a_max,a)
    #print(b_max,b)
    #print(c_max,c)
    #now, i've made sure "a" is the largest sequence. This minimizes the memory needed to store seqs

    len_lcs = []
    seqs = [] #list of actual lcs, now storing only 1 level deep
    seqs2 = [] #contains 2 row of sequences from diagonal line in lower level and for current line in lower level
    #set_seqs = set() #making sure we are not repeating any sequence in seqs[i][j][k]
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
                    seqs[j][k] = set([tuple([])]) #[[]] #setting all boundary points to list containing empty list
                else: #it means none of the indices are 0, so we are dealing with inside points
                    if (a[i-1]==b[j-1]) and (a[i-1]==c[k-1]): #using -1 since a,b,c are zero based
                        lcs_max = len_lcs[i-1][j-1][k-1] + 1 #since last element in each sequence matches, the len_lcs is 1 + len_lcs of the slightly smaller subsequences
                        #seqs[j][k] = [] #reset seqs for current indices
                        seqs[j][k] = set()
                        for l in seqs2[j2-1][k-1]: #now add the lcs values from smaller subsequences, appending this element to each
                            #ltemp = l[:]
                            #ltemp.append(a[i-1])
                            #ltemp = l + [a[i-1]]
                            #seqs[j][k].append(ltemp)
                            seqs[j][k].add(l + (a[i-1],))
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
                        #seqs[j][k] = [] #reset seqs for current indices
                        seqs[j][k] = set()
                        #set_seqs = set() #making sure we are not repeating any sequence in seqs[i][j][k]
                        if p1==lcs_max:
                            #print("seqs[i-1][j][k]", i-1, j, k, seqs[i2-1][j%2][k%2])
                            seqs[j][k] = seqs[j][k].union(seqs2[j2][k])
                        if p2==lcs_max:
                            #print("seqs[i][j-1][k]", i, j-1, k, seqs[i2][j%2-1][k%2])
                            seqs[j][k] = seqs[j][k].union(seqs[j-1][k])
                        if p3==lcs_max:
                            #print("seqs[i][j][k-1]", i, j, k-1, seqs[i2][j%2][k%2-1])
                            seqs[j][k] = seqs[j][k].union(seqs[j][k-1])
                        if p4==lcs_max:
                            #print("seqs[i][j-1][k-1]", i, j-1, k-1, seqs[i2][j%2-1][k%2-1])
                            seqs[j][k] = seqs[j][k].union(seqs[j-1][k-1])
                        if p5==lcs_max:
                            #print("seqs[i-1][j][k-1]", i-1, j, k-1, seqs[i2-1][j%2][k%2-1])
                            seqs[j][k] = seqs[j][k].union(seqs2[j2][k-1])
                        if p6==lcs_max:
                            #print("seqs[i-1][j-1][k]", i-1, j-1, k, seqs[i2-1][j%2-1][k%2])
                            seqs[j][k] = seqs[j][k].union(seqs2[j2-1][k])
                        #print("seqs[i][j][k]", i, j, k, seqs[i2][j%2][k%2])
                        #set_seqs.clear() #clearing set for next iteration
                    #print("lcs_max",lcs_max, "p1-6", p1, p2, p3, p4, p5, p6)
                    len_lcs[i][j].append(lcs_max)
    #print("printing lcs")
    #a_max2 = a_max%2
    for l in seqs[b_max][c_max]:
        #print("lcs= ", l)
        pass
    return len_lcs[a_max][b_max][c_max]


#using set instead of list, to store common subsequences, did not make a bit of difference to speed
#but because i used sets, i had to store common subsequences as tuple instead of list and that doubled my memory footprint
def lcs3_slow_big(a1, b1, c1): #also prints each lcs
    (c_max,c),(b_max,b),(a_max,a) = sorted([(len(a1),a1), (len(b1),b1), (len(c1),c1)])
    #print(a_max,a)
    #print(b_max,b)
    #print(c_max,c)
    #now, i've made sure "a" is the largest sequence. This minimizes the memory needed to store seqs

    len_lcs = []
    seqs = [] #list of actual lcs, now storing only 1 level deep
    seqs2 = [] #contains 2 row of sequences from diagonal line in lower level and for current line in lower level
    #set_seqs = set() #making sure we are not repeating any sequence in seqs[i][j][k]
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
                    seqs[j][k] = set([tuple([])]) #[[]] #setting all boundary points to list containing empty list
                else: #it means none of the indices are 0, so we are dealing with inside points
                    if (a[i-1]==b[j-1]) and (a[i-1]==c[k-1]): #using -1 since a,b,c are zero based
                        lcs_max = len_lcs[i-1][j-1][k-1] + 1 #since last element in each sequence matches, the len_lcs is 1 + len_lcs of the slightly smaller subsequences
                        #seqs[j][k] = [] #reset seqs for current indices
                        seqs[j][k] = set()
                        for l in seqs2[j2-1][k-1]: #now add the lcs values from smaller subsequences, appending this element to each
                            #ltemp = l[:]
                            #ltemp.append(a[i-1])
                            #ltemp = l + [a[i-1]]
                            #seqs[j][k].append(ltemp)
                            seqs[j][k].add(l + (a[i-1],))
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
                        #seqs[j][k] = [] #reset seqs for current indices
                        seqs[j][k] = set()
                        #set_seqs = set() #making sure we are not repeating any sequence in seqs[i][j][k]
                        if p1==lcs_max:
                            #print("seqs[i-1][j][k]", i-1, j, k, seqs[i2-1][j%2][k%2])
                            for l in seqs2[j2][k]:
                                seqs[j][k].add(l)
                        if p2==lcs_max:
                            #print("seqs[i][j-1][k]", i, j-1, k, seqs[i2][j%2-1][k%2])
                            for l in seqs[j-1][k]:
                                seqs[j][k].add(l)
                        if p3==lcs_max:
                            #print("seqs[i][j][k-1]", i, j, k-1, seqs[i2][j%2][k%2-1])
                            for l in seqs[j][k-1]:
                                seqs[j][k].add(l)
                        if p4==lcs_max:
                            #print("seqs[i][j-1][k-1]", i, j-1, k-1, seqs[i2][j%2-1][k%2-1])
                            for l in seqs[j-1][k-1]:
                                seqs[j][k].add(l)
                        if p5==lcs_max:
                            #print("seqs[i-1][j][k-1]", i-1, j, k-1, seqs[i2-1][j%2][k%2-1])
                            for l in seqs2[j2][k-1]:
                                seqs[j][k].add(l)
                        if p6==lcs_max:
                            #print("seqs[i-1][j-1][k]", i-1, j-1, k, seqs[i2-1][j%2-1][k%2])
                            for l in seqs2[j2-1][k]:
                                seqs[j][k].add(l)
                        #print("seqs[i][j][k]", i, j, k, seqs[i2][j%2][k%2])
                        #set_seqs.clear() #clearing set for next iteration
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
