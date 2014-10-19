
def memoryFunc(a,i,j):
	if a[i][j] is None: 
		memoryFunc(a,i,j) #produce result
		a[i][j] = result
	else:   result = a[i][j]
	return result

i = 0
j = 2
arr = [[None for x in xrange(5)] for x in xrange(5)]
memoryFunc(arr,i,j)

