import sklearn.datasets
print(sklearn.datasets.load_iris())
import math
def calculate_euclidean_norm(v):
        return math.hypot(*v)