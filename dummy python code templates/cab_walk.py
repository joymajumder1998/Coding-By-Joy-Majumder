import math

while(True):
    a=input().split(" ")
    if(int(a[0])>=1 and int(a[0])<=200):
        break
    if(int(a[1])>=1 and int(a[2])<=100):
        break 
n=float(a[0])
v1=float(a[1])
v2=float(a[2])
walk_distance=math.sqrt(2)*n
car_distance=n*2
walk_time=walk_distance/v1
car_time=car_distance/v2
if(car_time<walk_time):
    print("Cab")
else:
    print("Walk")