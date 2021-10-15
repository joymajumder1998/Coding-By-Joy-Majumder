import random

def search(a,k):
    pos=[]
    for i in range(len(a)):
        if(a[i]==k):
            pos.append(i)
    return pos

def getWord():
    words=["tiger","elephant","mafia","programming","water","morning"]
    s=random.choice(words)
    return  s

def play(player,point):
    print(player,"'s turn")
    word=list(getWord())
    dash=[]
    for i in range(len(word)):
        dash.append("-")
    i=0
    ch='1'
    print(dash)
    while(ch=='1'):
        l=input("Enter a letter : ")
        place=[]
        place=search(word,l)
        for i in range(len(place)):
            dash[place[i]]=l
        print(dash)
        ch=input("Want to guess another letter (1 to yes/0 to no) : ")
    ip=input("Guess the word : ")
    if(list(ip)==word):
        point=point+1
        print("Congratulation! you write correct word")
        print("Your point is : ",point) 
    else:
        print("OOPS Better luck next time :-(")
        print("Your point ",point)
    return point
#End of def play() 

def start():
    p1=input("Enter the name of player1 : ")
    p2=input("Enter the name of player2 : ")
    point1,point2=0,0
    count=0
    ch='1'
    while(ch=='1'):
        if(count%2==0):
            point1=play(p1,point1)
        else:
            point2=play(p2,point2)
            ch=input("Want to play more? (1 to yes/0 to no) :")
        count=count+1
       
start()