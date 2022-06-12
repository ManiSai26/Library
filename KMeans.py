# import matplotlib.pyplot as plt
# import pandas as pd
# import numpy as np
# from sklearn.cluster import KMeans
# df=pd.read_csv('iris.csv')
# kmeans=KMeans(n_clusters=3)
# coltypes=df.dtypes
# cols=len(coltypes)
# numcols=[]
# for d in range(cols):
#     if 'int' in str(coltypes[d]) or 'float' in str(coltypes[d]):
#         numcols.append(df.columns[d])
# for num in range(1,len(numcols)):
#     numcol=numcols[num]
#     x=[]
#     for k in range(df.shape[0]):
#         x.append([k,df.iloc[k][numcol]])
#     x=np.array(x)
#     print("True Position w.r.t attribute "+numcol)
#     plt.scatter(x[:,0],x[:,1],label='True Position')
#     plt.show()
#     print("ClusteredPoints w.r.t attribute "+numcol)
#     kmeans.fit(x)
#     plt.scatter(x[:,0],x[:,1],c=kmeans.labels_,cmap='rainbow')
#     plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],color='black')
#     plt.show()
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
df=pd.read_csv('iris.csv')
kmeans=KMeans(n_clusters=3)
coltypes=df.dtypes
cols=len(coltypes)
numcols=[]
for i in range(cols):
    if 'int' in str(coltypes[i]) or 'float' in str(coltypes[i]):
        numcols.append(df.columns[i])
for num in range(1,len(numcols)):
    numcol=numcols[num]
    x=[]
    for k in range(df.shape[0]):
        x.append([k,df.iloc[k][numcol]])
    x=np.array(x)
    print("True Position w.r.t "+numcol)
    plt.scatter(x[:,0],x[:,1],label='True Values') 
    plt.show()
    print("clustered Points of "+numcol)
    kmeans.fit(x)
    plt.scatter(x[:,0],x[:,1],c=kmeans.labels_,cmap='rainbow')
    plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],color='black')
    plt.show()