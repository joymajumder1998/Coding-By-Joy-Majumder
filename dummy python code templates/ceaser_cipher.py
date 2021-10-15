import string

myDict={}
for i in range(len(string.ascii_letters)):
    myDict[string.ascii_letters[i]]=string.ascii_letters[(i+1)%52]
with open("input.txt",'r') as fi:
    while True:
        c=fi.read(1)
        if not c:
            break
        if c in myDict:
            data=myDict[c]
        else:
            data=c
        print(data,end="")
fi.close()