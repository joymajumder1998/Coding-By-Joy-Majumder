def lkf(s:str,k):
    s=s.upper()
    l=[]
    for i in s:
        if(i!="-"):
            l.append(i)
    char=len(l)
    newdash=(char//k)-1
    size=char+newdash
    newl=[]
    if(char%2==0):
        j=0
        counter=0
        for index in range(size):
            if(counter==k):
                newl.append("-")
                counter=0
            else:
                newl.append(l[j])
                j=j+1
                counter=counter+1
    else:
        newl.append(l[0])
        newl.append("-")
        j=1
        counter=0
        for index in range(1,size):
            if(counter==k):
                newl.append("-")
                counter=0
            else:
                newl.append(l[j])
                j=j+1
                counter=counter+1
    return str(newl)