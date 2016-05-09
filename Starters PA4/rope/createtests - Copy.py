import sys
import random

from os import listdir
from os.path import isfile, join

mypath = sys.stdin.readline()
mypath = mypath[:-1] #to get rid of trailing new line

min_num = -10
max_num = 100
num_tests = 1000
num_segments = 1000
num_points = 100

#segments = []
#points = []
for j in range(num_tests):
    s = random.randint(1, num_segments) #number of segments
    p = random.randint(1, num_points) #number of points
    fname = mypath + "\\test" + str(j) + ".txt"
    with open(fname, 'w') as f:
        print(s,p)
        f.write(str(s) + " " + str(p) + "\n")
        for i in range(s):
            start_point = random.randint(min_num, max_num)
            end_point = random.randint(start_point, max_num)
            #segments.append(start_point + " " + end_point)
            print(start_point, end_point)
            f.write(str(start_point) + " " + str(end_point) + "\n")

        for i in range(p):
            point = random.randint(min_num, max_num)
            #points.append(point)
            print(point, end=' ')
            f.write(str(point) + " ")

        print("\n-----------------------------------")
        f.write("\n")
