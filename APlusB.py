# Uses python3
import sys

input = sys.stdin.readline()
tokens = input.split()
a = int(tokens[0])
b = int(tokens[1])
if ((a >= 0) and (a <= 9) and (b >= 0) and (b <= 9)):
	print(a + b)
