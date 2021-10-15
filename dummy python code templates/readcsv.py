import csv

with open("route.csv","r") as f:
    reader=csv.reader(f)
    for row in reader:
        print(row)
f.close()