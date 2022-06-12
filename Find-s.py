import csv
a=[]
with open('enjoysport.csv') as csvfile:
    data=csv.reader(csvfile)
    for i in data:
        a.append(i)
n=len(a)-1
attr=len(a[0])-1
h=['0']*attr
for i in range(1,n+1):
    if(a[i][attr]=='yes'):
        for j in range(attr):
            if(h[j]=='0'):
                h[j]=a[i][j]
            if(h[j]!=a[i][j]):
                h[j]='?'
    print(", ".join(h))