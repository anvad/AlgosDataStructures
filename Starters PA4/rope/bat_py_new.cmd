@echo off
echo rope_new.py before: %time%
py -3 rope_new.py <%1\test0.txt >out_py_new.txt
echo rope_new.py after: %time%
