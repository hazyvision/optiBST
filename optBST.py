#Written by Adriene Cuenco
#CS331 Fall2014 Due: 10/24/14 + 24 hours ext.

#!/usr/bin/python
#Python Version: 3.3.5

#Optimal Binary Search Tree
#Input: A list of probabilities with a corresponding list of keys
#Output: The list of probabilities, minimum average of search time, 
#        and the optimal binary search tree

def findMin(i,j):
	indexLow = 0
	sumLow =  100
	for x in range(i,j+1):
		test = A(i,x-1) + A(x+1,j) 
		if sumLow > test:
			sumLow=test 
			indexLow = x
	return indexLow

def A(i,j):
	if a[i][j] is None: 
		if j is i-1:  
			result = 0
			a[i][j] = result
			r[i][j] = result
			return result
		if i is j:
			result = prob[i-1]
			a[i][j] = result
			r[i][j] = i
			return result
		result = A(i,k-1) + A(k+1,j) + sumProb(i,j)
		a[i][j] = result
	else:
		result = a[i][j]
	return result

def sumProb(i, j):
	sum = 0
	for x in range(i,j+1):
		sum+=prob[x-1]
	return sum 

def optBST(n, p):
	 global k
	 global r
	 for d in range(1,n):
	 	for i in range(1,(n-d) + 1 ):
	 		j = i + d
	 		k = findMin(i,j)
	 		A(i , j)
	 		r[i][j]=k
	 return;

def toString(i,j):
	global r
	global n
	leftList = [None for x in range(j+1)]
	rightList = [None for x in range(j+1)]
	for x in range(1,j+1):
		leftList[x] = r[1][x]
	for x in range(j+1):
		rightList[x] = r[x][j]
	leftList= list(set(leftList))   #make list unique
	leftList = list(filter(None.__ne__, leftList)) #remove None spaces
	leftList.reverse() #reverse list
	rightList= list(set(rightList)) #make list unique
	rightList = list(filter(None.__ne__, rightList)) #remove None spaces
    #make lists same size
	s =""
	if len(leftList) < len(rightList):
		addSpace=len(rightList) - len(leftList)
		leftList.extend([None]*addSpace)
	if len(rightList) < len(leftList):
		addSpace=len(leftList) - len(rightList) 
		rightList.extend([None]*addSpace)
	#Build String (optimal BST)
	s += "(" + keys[leftList[0]-1]
	for x in range(1,len(leftList)): 	
		if leftList[x] is not None and rightList[x] is not None:
			s += "(" + keys[leftList[x]-1] + ", " + keys[rightList[x]-1]   
		if leftList[x] is None and rightList[x] is not None:
			s += "(" + ", " +  keys[rightList[x]-1]
		if leftList[x] is not None and rightList[x] is None:
			s += "("+ keys[leftList[x]-1] + ", "
	#Add closing parenthesis
	for x in range(1,len(leftList)):
		s += ")" 
	return s; 

def reset():
	global a
	global r
	a = [[None for x in range(n+1)] for y in range(n+2)]
	r = [[None for x in range(n+1)] for y in range(n+2)]
	return;

#***********main*******************************
#------------Instance 1------------------------
prob = [3/8, 3/8, 1/8, 1/8 ]
keys = ["Don", "Isabelle", "Ralph", "Wally"]
n = len(keys) 
a = [[None for x in range(n+1)] for y in range(n+2)]
r = [[None for x in range(n+1)] for y in range(n+2)]
optBST(n, prob)
print(prob)
print(a[1][n])
print(toString(1,n))
print()

#------------Instance 2------------------------
prob = [0.1, 0.2, 0.4, 0.3 ]
keys = ["A", "B", "C", "D"]
n = len(keys) 
reset()
optBST(n, prob)
print(prob)
print(a[1][n])
print(toString(1,n))
print()

#-----------Instance 3------------------------
p=float("{0:.3}".format(1/7))
prob = [p, p, p, p, p, p, p ]
keys = ["A", "B", "C", "D","E","F","G"]
n = len(keys) 
reset()
optBST(n, prob)
print(prob)
print("{0:.3}".format(a[1][n]))
print(toString(1,n))
print()
