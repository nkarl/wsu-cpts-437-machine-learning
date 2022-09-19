import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn import neighbors, datasets

n_neighbors = 1

# bc = datasets.load_breast_cancer()
red = [(0, 1), (2, 3), (4, 4)]
blue = [(2, 0), (5, 2), (6, 3)]

class Point:
    x = 0.0
    y = 0.0
    c = ''


Red = list()
for p in red:
    n = Point()
    n.x = p[0]
    n.y = p[1]
    n.c = 'red'
    Red.append(n)

Blue = list()
for p in blue:
    n = Point()
    n.x = p[0]
    n.y = p[1]
    n.c = 'blue'
    Blue.append(n)


X = Red
y = Blue


cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF'])
cmap_bold = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])

clf = neighbors.KNeighborsClassifier(n_neighbors)
clf.fit(X, y)

x_min, x_max = X[0].min() - 1, X[-1].max() + 1
y_min, y_max = y[0].min() - 1, y[-1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, .02), np.arange(y_min, y_max,
                                                             .02))

Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])

Z = Z.reshape(xx.shape)
plt.figure()
plt.pcolormesh(xx, yy, Z, cmap=cmap_light)

plt.scatter(X[0], X[-1], c=y, cmap=cmap_bold, edgecolor='k', s=20)
plt.xlim(xx.min(), xx.max())
plt.ylim(yy.min(), yy.max())
plt.title('Binary class. (k=%i)' % (n_neighbors))
