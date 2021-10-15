def AStarSearch():
    n=int(input("Enter the number of nodes : "))
    aug=[[[]for i in range(n)]for j in range(n)]
    print("Enter the augmented matrix : ")
    for i in range(n):
        for j in range(n):
            print("Enter A[",i,"][",j,"] : ",end="")
            aug[i][j]=int(input())
    initial=int(input("Enter the initial node : "))
    OPEN=initial
    GOAL=int(input("Enter the goal node : "))
    if(OPEN==GOAL):
       exit
    a=OPEN
    if(a==GOAL):
        return