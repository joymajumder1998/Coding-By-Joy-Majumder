n=input()
n=list(n)
count0=0
count1=0
for i in n:
    if(i=='0'):
        count0=count0+1
    if(i=='1'):
        count1=count1+1
if(count0<=1 or count1<=1):
    print("YES")
else:
    print("NO")