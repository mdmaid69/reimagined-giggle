import sklearn.datasets
print(sklearn.datasets.load_iris())
import math
def calculate_polar_to_cartesian_coordinates(r, theta):
        return math.polar((r, theta))