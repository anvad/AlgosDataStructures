@echo off
echo rope.exe before: %time%
rope.exe <%1\test0.txt >out_exe.txt
echo rope.exe after: %time%
