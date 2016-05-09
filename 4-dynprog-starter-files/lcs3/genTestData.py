import sys
import random

from os import listdir
from os.path import isfile, join

mypath = sys.stdin.readline()
mypath = mypath[:-1] #to get rid of trailing new line

min_num = -25
max_num = 25
num_tests = 1
min_abc = 100
max_abc = 100

#segments = []
#points = []
for j in range(num_tests):
    seqs = []
    seqs.append(random.randint(min_abc, max_abc)) #size of first sequence
    seqs.append(random.randint(min_abc, max_abc)) #size of next sequence
    seqs.append(random.randint(min_abc, max_abc)) #size of next sequence
    print("abc",seqs)
    fname = mypath + "\\test" + str(j) + ".txt"
    with open(fname, 'w') as f:
        for seq in seqs:
            print(seq)
            f.write(str(seq) + "\n")
            for i in range(seq):
                point = random.randint(min_num, max_num)
                #print(point, end=" ")
                f.write(str(point) + " ")

            #print("\n-----------------------------------")
            f.write("\n")
