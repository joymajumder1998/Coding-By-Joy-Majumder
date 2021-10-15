T=int(input())
for case in range(T):
    A,B=map(int,input().split(" "))
    N=int(input())
    for exchange in range(N):
        Q=(A+B)//2
        print(Q)
        correct=False
        text=input()
        if(text=="CORRECT"):
            correct=True
            break
        #End if
        if(text=="TOO_SMALL"):
            A=Q+1
        if(text=="TOO_BIG"):
            B=Q-1
    #End for
    if(correct==False):
        print("WRONG_ANSWER")
#End for