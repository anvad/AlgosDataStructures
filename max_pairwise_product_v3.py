# Uses python3
n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)



def MaxPairwiseProduct( a ):
	n = len(a)
	result = 0
	for i in range(0, n):
		for j in range(i+1, n):
			if a[i]*a[j] > result:
				result = a[i]*a[j]
	return result

def MaxPairwiseProductFast( numbers ):
	n = len(numbers)
	maxIndex1 = 0
	for i in range(0, n):
		if (numbers[i] > numbers[maxIndex1]):
			maxIndex1 = i
	maxIndex2 = 0
	if (maxIndex1 == 0):
		maxIndex2 = 1
	for j in range(0, n):
		if ( (numbers[j] > numbers[maxIndex2]) and (j != maxIndex1) ):
			maxIndex2 = j
	return numbers[maxIndex1] * numbers[maxIndex2]

#result = MaxPairwiseProduct(a)
result2 = MaxPairwiseProductFast(a)

#print(result)
print(result2)
