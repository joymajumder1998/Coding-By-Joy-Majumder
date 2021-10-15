ip=input().split(' ')
r=int(ip[0])
c=int(ip[1])
x=1
a=[[[]for i in range(c)]for j in range(r)]
for i in range(r):
    for j in range(c):
        a[i][j]=x
        x=x+1
for i in range(r):
    for j in range(c):
        if(j==0):
            print(a[i][j],end='') 
        else:
            print(" %s"%(a[i][j]),end='')
    if(i!=r-1):    
        print()