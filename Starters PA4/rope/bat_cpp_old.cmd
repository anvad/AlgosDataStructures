@echo off
echo rope_old.exe before: %time%
rope_old.exe <%1\test0.txt >out_exe_old.txt
echo rope_old.exe after: %time%
