n=int(input())
a=input().split(" ")
b=[None]*n
for i in range(n):
	b[i]=a[i]
b.reverse()
c=[None]*n
for i in range(n):
	c[i]=int(a[i])+int(b[i])
for i in range(n):
	print(c[i],end=" ")
