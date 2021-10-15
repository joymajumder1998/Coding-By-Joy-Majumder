def ifPrime(n):
    count=0
    for i in range(1,n):
        if(n%i==0):
            count=count+1
    if(count==1):
        return True
    else:
        return False
    
def ifSemiPrime(n):
    for i in range(2,n):
        for j in range(2,n):
            if(i*j==n):
                if(ifPrime(i)==False or ifPrime(j)==False or i==j):
                    return False
    return True

def check(n):
    for i in range(3,n):
        for j in range(3,n):
            if(i+j==n):
                if(ifSemiPrime(i)==True and ifSemiPrime(j)==True):
                    return "Yes"
    return "No"

n=int(input())
print(check(n))