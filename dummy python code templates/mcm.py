#Read the number of the matrix
n=int(input("Enter the number of matrices : "))
#Read the sizes of the matrices and assign it at d[] array
d=[None]*(n+1)
for i in range(1,n+1):
	print(f"\n{i}-Th Matrix :- ")
	d[i-1]=int(input("Enter the number of row : "))
	d[i]=int(input("Enter the number of coloumn : "))
#create the table for dynamic programming
p=[[[]for i in range(0,n+1)]for j in range(0,n+1)]
#Start the algorithm
for i in range(1,n+1):
	p[i][i]=0
for s in range(1,n):
	for i in range(1,n-s+1):
		j=i+s
		p[i][j]=99999
		for k in range(i,j):
			mini=int(p[i][k])+int(p[k+1][j])+d[i-1]*d[k]*d[j]
			if(mini<int(p[i][j])):
				p[i][j]=mini;	
for i in range(1,n+1):
	for j in range(1,n+1):
		t=p[i][j]
		print("%4s"%(t),end="")
	print()
