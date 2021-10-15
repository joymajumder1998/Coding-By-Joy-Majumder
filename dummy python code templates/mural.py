def calculate():
    score.append(max(parts))
    pos=parts.index(max(parts))
    parts[pos]=-99
    for i in range(N//2):
        
    #End for
    if(N%2==1):
        score.append(parts[0])

T=int(input())
for i in range(T):
    N=int(input())
    parts=[0]*N
    string=input()
    for k in range(N): 
        parts[k]=int(string[k])
    score=[0]
    calculate()
    result=sum(score)
    print("Case #",i+1,": ",result) 
#End for