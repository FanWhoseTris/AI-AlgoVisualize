from sklearn.cluster import KMeans
from sklearn import datasets
import matplotlib.pyplot as plt

iris = datasets.load_iris()

iris_X = iris.data
iris_Y = iris.target
print(iris_Y)
plt.hist(iris_Y)
plt.show()
