import sklearn.datasets
print(sklearn.datasets.load_iris())
import math
def calculate_euclidean_distance(p, q):
        return math.dist(p, q)