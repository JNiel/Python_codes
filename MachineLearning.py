# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 11:39:35 2016

@author: jon.nielsen
"""

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn import datasets
from sklearn.decomposition import PCA
from scipy import optimize
import numpy as np

#import data to use for learning methods
iris = datasets.load_iris()
X = iris.data[:, :2] #Only the first two features
Y = iris.target

x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5
y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5

plt.figure(2, figsize= (8, 6))
plt.clf()

#Plot the training points
plt.scatter(X[:, 0], X[:, 1], c=Y, cmap=plt.cm.Paired)
plt.xlabel('Sepal length')
plt.ylabel('Sepal width')

plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xticks(())
plt.yticks(())

#To get a better understanding of interaction of the dimensions, plot the first 3 PCA dimensions.
fig = plt.figure(1, figsize=(8, 6))
ax = Axes3D(fig, elev=-150, azim=110)
X_reduced = PCA(n_components=3).fit_transform(iris.data)
ax.scatter(X_reduced[:, 0], X_reduced[:, 1], X_reduced[:, 2], c=Y, cmap=plt.cm.Paired)
ax.set_title('First three PCA directions')
ax.set_xlabel('First eigenvector')
ax.w_xaxis.set_ticklabels([])
ax.set_ylabel('Second eigenvector')
ax.w_yaxis.set_ticklabels([])
ax.set_zlabel('Third eigenvector')
ax.w_zaxis.set_ticklabels([])

plt.show()


from matplotlib.colors import ListedColormap
from sklearn import neighbors, datasets

n_neighbors = 15

h= .02 #Step size in the mesh

#Create color maps.
cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF'])
cmap_bold = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])

for weights in ['uniform', 'distance']:
    #Create an instance of neighbors classifier and fit the data
    clf = neighbors.KNeighborsClassifier(n_neighbors, weights=weights)
    clf.fit(X, y)
    
    #Plot the decision boundary. For that we will assign a color to each point in the mesh [x_min, m_max]x[y_min, y_max].
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    
    #Put the result into a color plot
    Z = Z.reshape(xx.shape)
    plt.figure(3, figsize = (8, 6))
    plt.pcolormesh(xx, yy, Z, cmap = cmap_light)
    
    #Plot the training points
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap=cmap_bold)
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())
    plt.title("3-class classification (k = %i, weights = '%s')" % (n_neighbors, weights))

plt.show()





