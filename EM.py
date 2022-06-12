import matplotlib.pyplot as plt
from sklearn import datasets
import pandas as pd
import numpy as np
iris = datasets.load_iris()
X = pd.DataFrame(iris.data)
X.columns = ['Sepal_Length','Sepal_Width','Petal_Length','Petal_Width']
y = pd.DataFrame(iris.target)
y.columns = ['Targets']
colormap = np.array(['red', 'lime', 'black'])
plt.figure(figsize=(7,10))
plt.subplot(2, 1, 1)
plt.scatter(X.Sepal_Length, X.Sepal_Width, c=colormap[y.Targets], s=40)
plt.title('Real Clusters')
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
from sklearn import preprocessing
scaler = preprocessing.StandardScaler()
scaler.fit(X)
xsa = scaler.transform(X)
xs = pd.DataFrame(xsa, columns = X.columns)
from sklearn.mixture import GaussianMixture
gmm = GaussianMixture(n_components=3)
gmm.fit(xs)
gmm_y = gmm.predict(xs)
#print("mean:\n",gmm.means_)
#print('\n')
#print("Covariances\n",gmm.covariances_)
plt.subplot(2, 1, 2)
plt.scatter(X.Sepal_Length, X.Sepal_Width, c=colormap[gmm_y], s=40)
plt.title('GMM Clustering using EM')
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.show()