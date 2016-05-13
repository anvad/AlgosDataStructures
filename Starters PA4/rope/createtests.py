import sys
import random

from os import listdir
from os.path import isfile, join

mypath = sys.stdin.readline()
mypath = mypath[:-1] #to get rid of trailing new line

num_tests = 1 #1000
slen = 300000

#st = "hello,world.Iamastringsplicerworkingmymagic,exceptiamnotworkverywellrightnow."
#st = "hello,world.Iamastringspl"
#st = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbaaaaaaaaaaaaaabababababababa"
#slen = len(st)

alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

stList = [alpha[random.randint(0,51)] for i in range(slen)]
st = "".join(stList)

#segments = []
#points = []
for j in range(num_tests):
    #q = random.randint(1, 500) #number of queries
    q = 100000
    fname = mypath + "\\test" + str(j) + ".txt"
    with open(fname, 'w') as f:
        f.write(st + "\n")
        f.write(str(q) + "\n")
        for i in range(q):
            s = random.randint(0, (slen - 1)//2) #starting index
            #e = random.randint(s, min((s + 6), (slen - 1))) #ending index
            e = random.randint(s, slen) #ending index
            k = random.randint(0, (slen - (e - s + 1)))
            #print(s, e, k)
            f.write(str(s) + " " + str(e) + " " + str(k) + "\n")
        print("\n-----------------------------------")
        #f.write("\n")

fname_cpp = "bat_cpp.cmd"
fname_py = "bat_py.cmd"
fname_naive_py = "bat_py_naive.cmd"

with open(fname_cpp, 'w') as f:
    f.write("@echo off\n")
    f.write("echo rope.exe before: %time%\n")
    for j in range(num_tests):
        fname = "%1\\test" + str(j) + ".txt"
        f.write("rope.exe <" + fname + " >out_exe.txt\n")
    f.write("echo rope.exe after: %time%\n")

with open(fname_py, 'w') as f:
    f.write("@echo off\n")
    f.write("echo rope.py before: %time%\n")
    for j in range(num_tests):
        fname = "%1\\test" + str(j) + ".txt"
        f.write("py -3 rope.py <" + fname + " >out_py.txt\n")
    f.write("echo rope.py after: %time%\n")
        
with open(fname_naive_py, 'w') as f:
    f.write("@echo off\n")
    f.write("echo naive before: %time%\n")
    for j in range(num_tests):
        fname = "%1\\test" + str(j) + ".txt"
        f.write("py -3 rope_naive.py <" + fname + " >out_naive_py.txt\n")
    f.write("echo naive after: %time%\n")