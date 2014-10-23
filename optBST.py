
#Written by Adriene Cuenco

#!/usr/bin/python

#Optimal Binary Search Tree
#Input: A list of probabilities with a corresponding list of keys
#Output: The list of probabilities, minimum average of search time, 
#        and the optimal binary search tree

def memoryFunc(a,i,j):
	if a[i][j] is None: 
		result = a[i][i-1] + a[i+1][j] + sumProb(a,i,j)  
		a[i][j] = result
	else:   result = a[i][j]
	return result

def sumProb(a, i, j):
	sum = 0
	j+=1
	for x in range(i,j):
	  sum+=prob[x]
	return sum 


def optBST(n , p, r):
	 a = [[None for x in range(n+1)] for y in range(n+2)]
	 for i in range(1,n):
	 	a[i][i-1] = 0
	 	a[i][i] = p[i]
	 	r[i][i] = i
	 	r[i][i-1] = 0

	 a[n+1][n] = 0
	 r[n+1][n] = 0

	 for diagonal in range(1,n-1):
	 	for i in range(1, n-diagonal):
	 		j = i + diagonal
	 		memoryFunc(a, i , j)
	 		r[i][j] = i
	 minavg = a
	 print(minavg)
	 #Extra prints for debug. Delete before submission.
	 print("r = ") 
	 print(r)
	 print("n = ")
	 print(n)
	 return;

prob = [None, 3/8, 3/8, 1/8, 1/8 ]
keys = [None, "Don", "Isabelle", "Ralph", "Wally"]
n = len(keys) - 1 
r = [[None for x in range(n+1)] for y in range(n+2)] 
optBST(n, prob, r)












