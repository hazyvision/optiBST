#Written by Adriene Cuenco
#CS331 Fall2014 Due: 10/24/14

#!/usr/bin/python

#Optimal Binary Search Tree
#Input: A list of probabilities with a corresponding list of keys
#Output: The list of probabilities, minimum average of search time, 
#        and the optimal binary search tree

def findMin(a,i,j):
	indexLow = 0
	sumLow =  100
	for x in range(i,j+1):
		test = a[i][x-1] + a[x+1][j]
		if sumLow > test:
			sumLow=test 
			indexLow = x
	return indexLow

def memory(a,i,j):
	if a[i][j] is None: 
		result = a[i][k-1] + a[k+1][j] + sumProb(i,j) #RecurrenceRelation goes here
		a[i][j] = result
	else:   
		result = a[i][j]
	return result

def sumProb(i, j):
	sum = 0
	for x in range(i,j+1):
		sum+=prob[x-1]
	return sum 

def optBST(n, p, r):
	 global a
	 global k
	 for i in range(1,n+1):
	 	a[i][i-1] = 0
	 	a[i][i] = p[i-1]
	 	r[i][i] = i
	 	r[i][i-1] = 0
	 	
	 a[n+1][n] = 0
	 r[n+1][n] = 0
	 for diagonal in range(1,n):
	 	for i in range(1,(n-diagonal) + 1 ):
	 		j = i + diagonal
	 		k = findMin(a,i,j)
	 		memory(a, i , j)
	 		r[i][j] = k
	 return;

#***********main*******************************
prob = [3/8, 3/8, 1/8, 1/8 ]
keys = ["Don", "Isabelle", "Ralph", "Wally"]
n = len(keys) 
a = [[None for x in range(n+1)] for y in range(n+2)]
r = [[None for x in range(n+1)] for y in range(n+2)]
optBST(n, prob, r)
print(prob)
print(a[1][n])