import numpy as np
import pandas as pd
iris=pd.read_csv('iris.csv')
testset=pd.DataFrame([4.6,3.2,1.4,0.2])
def ed(trainset,testset):
    s=0
    for i in range(1,5):
        s+=np.square(float(trainset.iloc[i])-float(testset.iloc[i-1]))
    return np.sqrt(s)
def knn(trainset,testset,k):
    distances=[]
    for  i in range(len(trainset)):
        dis=ed(trainset.iloc[i],testset)
        distances.append([trainset.iloc[i][5],dis])
    distances.sort(key=lambda x:x[1])
    distances=distances[:k]
    votes={}
    for i in distances:
        votes[i[0]]=votes.get(i[0],0)+1
    res=max(votes.items(),key=lambda x:x[1])
    print(res)
knn(iris,testset,4)