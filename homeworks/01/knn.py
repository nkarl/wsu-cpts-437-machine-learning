import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn import neighbors, datasets

n_neighbors = 1

# bc = datasets.load_breast_cancer()
red = [(0, 1), (2, 3), (4, 4)]
blue = [(2, 0), (5, 2), (6, 3)]

points = red + blue

x, y = zip(*points)
plt.scatter(x, y)
