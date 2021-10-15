import matplotlib.pyplot as plt

#this function draw a point at (x,y) position
def putpixel(x,y):
    plt.plot([x],[y],'ro',markersize=3)
    
x1=int(input("x1 : "))
y1=int(input("y1 : "))
x2=int(input("x2 : "))
y2=int(input("y2 : "))
#algo of dda line drawing alggorithm
dx=abs(x2-x1)
dy=abs(y2-y1) 
if(dx>=dy):
    steps=dx
else:
    steps=dy
xinc=dx/steps
yinc=dy/steps
x=x1
y=y1
xp=[]
yp=[]
for i in range(1,steps+1):
    putpixel(x,y)
    x=x+xinc
    y=y+yinc
#end of the algorithm
plt.plot([0,100],[0,100],'wo')#size the plot from(0,0) to(80,80)
plt.show()#display the graph plot