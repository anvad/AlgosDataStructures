@echo off
echo rope.py before: %time%
py -3 rope.py <%1\test0.txt >out_py.txt
echo rope.py after: %time%
