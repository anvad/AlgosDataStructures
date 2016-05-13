@echo off
echo naive before: %time%
py -3 rope_naive.py <%1\test0.txt >out_naive_py.txt
echo naive after: %time%
