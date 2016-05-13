@echo off
echo rope_old.py before: %time%
py -3 rope_old.py <%1\test0.txt >out_py_old.txt
echo rope_old.py after: %time%
