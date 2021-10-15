a=map(int,input().split(" "))
n=len(a)
count=0
for i in range(n):
    flag=1
    for j in range(n-i-1):
        if(a[j]>a[j+1]):
            a[j],a[j+1]=a[j+1],a[j]
            flag=0
    count=count+1
    if(flag==1):
        break
if(count==1):
    count=0
print(count)